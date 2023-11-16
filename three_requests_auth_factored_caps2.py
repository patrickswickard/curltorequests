import requests
import re
import json
import shutil
import mysecret
import time
import instapost

#username = 'vintage_bmore_graffiti'
#username = 'cannibal_corpse_limericks'
username = 'bugbobbie'
#username = 'dont_fear_the_millimeter'

secret = mysecret.Mysecret()
sessionid = secret.sid

# method to download a single photo, takes url as source and dl target as filename
def download_single_photo(source,filename):
  source = source
  photo_filename = filename
  url_response = requests.get(source, stream=True)
  with open(photo_filename, 'wb') as out_file:
    shutil.copyfileobj(url_response.raw, out_file)

# method to get app id parameter which is probably static but maybe not?
# in any case it is parsable at least for now
# if this breaks try hard-coding it
def get_app_id(username):
  debug = False
  request_url = 'https://www.instagram.com/' + username + '/'
  headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0'}
  if not debug:
    proxies = {}
  else:
    proxies = {
      'http' : 'http://localhost:8888',
      'https' : 'http://localhost:8888',
    }
  response = requests.get(request_url, headers=headers, proxies=proxies, verify=False)
  raw_html = response.text
  responselines = response.text.splitlines()
  for thisline in responselines:
    hit = re.search(r"APP_ID",thisline)
    if hit:
      jsonthisline = re.findall(r"<script[^>]*>\s*(.*?)\s*</script>",thisline)
      if jsonthisline:
        jsontext = jsonthisline[0]
        # this json is so disorganized it's not even worth parsing
        #thishash = json.loads(jsontext)
        app_id_hits = re.findall(r"\"APP_ID\":\"(.*?)\"",jsontext)
        app_id = app_id_hits[0]
        return app_id

def get_first_set(username,app_id,sessionid):
  request_url = 'https://www.instagram.com/api/v1/users/web_profile_info/?username=' + username
  header_hash = {
  }
  # this is probably hard-coded but we parse it anyway
  # if/when this breaks try the hard-coded version
  #header_hash['x-ig-app-id'] = '936619743392459'
  header_hash['Cookie'] = 'sessionid=' + sessionid + '; ds_user_id=CAFE'
  header_hash['x-ig-app-id'] = app_id
  headers = header_hash
  response = requests.get(request_url, headers=headers)
  response_hash = json.loads(response.text)
#  outfilename = 'FIRSTSET.json'
#  thisoutfile = open(outfilename, 'w')
#  thisoutfile.write(response.text)
  return response_hash

def list_links_from_response_hash(response_hash):
  batch_list = []
  data = response_hash['data']
  user = data['user']
  edge_owner_to_timeline_media = user['edge_owner_to_timeline_media']
  page_info = edge_owner_to_timeline_media['page_info']
  edges = edge_owner_to_timeline_media['edges']
  has_next_page = page_info['has_next_page']
  end_cursor = ''
  if has_next_page:
    end_cursor = page_info['end_cursor']
  for thisedge in edges:
    node = thisedge['node']
    post_object = instapost.Instapost()
    post_object.process_post(node)
    if post_object.sidecar_to_children_list:
      for my_post_object in post_object.sidecar_to_children_list:
        batch_list.append(my_post_object.display_url)
    else:
      batch_list.append(post_object.display_url)
  return batch_list

def list_data_from_response_hash(response_hash):
  batch_list = []
  data = response_hash['data']
  user = data['user']
  edge_owner_to_timeline_media = user['edge_owner_to_timeline_media']
  page_info = edge_owner_to_timeline_media['page_info']
  edges = edge_owner_to_timeline_media['edges']
  has_next_page = page_info['has_next_page']
  end_cursor = ''
  if has_next_page:
    end_cursor = page_info['end_cursor']
  for thisedge in edges:
    node = thisedge['node']
    post_object = instapost.Instapost()
    post_object.process_post(node)
    if post_object.sidecar_to_children_list:
      for my_post_object in post_object.sidecar_to_children_list:
        #batch_list.append(my_post_object.display_url)
        batch_list.append(my_post_object.dumph())
        #batch_list.append(my_post_object.dumph(self))
    else:
      #batch_list.append(post_object.display_url)
      batch_list.append(post_object.dumph())
      #batch_list.append(post_object.type())
  return batch_list

def get_user_id_from_response_hash(response_hash):
  data = response_hash['data']
  user = data['user']
  user_id = user['id']
  return user_id

def get_end_cursor_from_response_hash(response_hash):
  data = response_hash['data']
  user = data['user']
  edge_owner_to_timeline_media = user['edge_owner_to_timeline_media']
  page_info = edge_owner_to_timeline_media['page_info']
  has_next_page = page_info['has_next_page']
  end_cursor = ''
  if has_next_page:
    end_cursor = page_info['end_cursor']
  return end_cursor

def get_next_response_hash(doc_id,app_id,user_id,end_cursor,num,sessionid):
  if end_cursor:
    request_url = 'https://www.instagram.com/graphql/query/?doc_id=' + doc_id + '&variables=%7B%22id%22%3A%22' + user_id + '%22%2C%22after%22%3A%22' + end_cursor + '%22%2C%22first%22%3A' + num + '%7D'
    header_hash = {
    }
    header_hash['Cookie'] = 'sessionid=' + sessionid + '; ds_user_id=CAFE'
    header_hash['x-ig-app-id'] = app_id
    headers = header_hash
    response = requests.get(request_url, headers=headers)
    response_hash = json.loads(response.text)
    outfilename = 'NEXTSET.json'
    thisoutfile = open(outfilename, 'w')
    thisoutfile.write(response.text)
    return response_hash

# this method is great but really want a method that gets all post info and returns that
# then another method that can maybe take that and spit out all photos
def get_all_photos_list(username, sessionid):
  all_photos_list = []
  app_id = get_app_id(username)
  response_hash = get_first_set(username,app_id,sessionid)
  this_list = list_links_from_response_hash(response_hash)
  all_photos_list = all_photos_list + this_list

  # hard-coded, hopefully always the same
  doc_id = '17991233890457762'
  user_id = get_user_id_from_response_hash(response_hash)
  end_cursor = get_end_cursor_from_response_hash(response_hash)
  num = '50'

  while end_cursor:
    next_response_hash = get_next_response_hash(doc_id,app_id,user_id,end_cursor,num,sessionid)
    this_list = list_links_from_response_hash(next_response_hash)
    all_photos_list = all_photos_list + this_list
    doc_id = '17991233890457762'
    user_id = user_id
    end_cursor = get_end_cursor_from_response_hash(next_response_hash)
    num = '50'
  return all_photos_list

#################################################################

# this method is great but really want a method that gets all post info and returns that
# then another method that can maybe take that and spit out all photos
def get_all_data_list(username, sessionid):
  all_data_list = []
  app_id = get_app_id(username)
  response_hash = get_first_set(username,app_id,sessionid)
  this_list = list_data_from_response_hash(response_hash)
  all_data_list = all_data_list + this_list

  # hard-coded, hopefully always the same
  doc_id = '17991233890457762'
  user_id = get_user_id_from_response_hash(response_hash)
  end_cursor = get_end_cursor_from_response_hash(response_hash)
  num = '50'

  while end_cursor:
    next_response_hash = get_next_response_hash(doc_id,app_id,user_id,end_cursor,num,sessionid)
    this_list = list_data_from_response_hash(next_response_hash)
    all_data_list = all_data_list + this_list
    doc_id = '17991233890457762'
    user_id = user_id
    end_cursor = get_end_cursor_from_response_hash(next_response_hash)
    num = '50'
  return all_data_list

#all_photos_list = get_all_photos_list(username, sessionid)
all_data_list = get_all_data_list(username, sessionid)

#print(json.dumps(all_photos_list))
print(json.dumps(all_data_list))
outfilename = 'all_data_list.json'
thisoutfile = open(outfilename, 'w')
#thisoutfile.write(json.dumps(all_photos_list))
thisoutfile.write(json.dumps(all_data_list))

for entry in all_data_list:
  print('******************************************************')
  print('******************************************************')
  print(entry['display_url'])
