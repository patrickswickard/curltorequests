import requests
import re
import json
import shutil
import mysecret
import time
import instapost

#username = 'vintage_bmore_graffiti'
#username = 'cannibal_corpse_limericks'
#username = 'bugbobbie'
username = 'dont_fear_the_millimeter'

secret = mysecret.Mysecret()
sessionid = secret.sid
print(sessionid)

all_photos_list = []

# method to download a single photo, takes url as source and dl target as filename
def download_single_photo(source,filename):
  source = source
  photo_filename = filename
  url_response = requests.get(source, stream=True)
  with open(photo_filename, 'wb') as out_file:
    shutil.copyfileobj(url_response.raw, out_file)

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
  return response_hash

def print_links_from_response_hash(response_hash):
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
    display_url = node['display_url']
    print(display_url)

def process_post(thispost):
  dimensions = thispost.get('dimensions',{})
  if dimensions:
    height = dimensions.get('height','')
    width = dimensions.get('width','')
  display_url = thispost.get('display_url','')
  is_video = thispost.get('is_video',False)
  tagged_user_list = thispost.get('edge_media_to_tagged_user',[])
  accessibility_caption = thispost.get('accessibility_caption','')
  caption = ''
  if thispost.get('edge_media_to_caption',''):
    captionlist = thispost['edge_media_to_caption']['edges']
    if captionlist:
      caption = captionlist[0]
  userid = ''
  username = ''
  owner = thispost.get('owner',{})
  if owner:
    userid = owner.get('id','')
    username = owner.get('username','')
  location = thispost.get('location','')
  posts_beyond_first = []
  sidecar_to_children_list = []
  sidecar_to_children = thispost.get('edge_sidecar_to_children',{})
  if sidecar_to_children:
    sidecar_to_children_list = sidecar_to_children.get('edges',[])
    if sidecar_to_children_list:
      for thissubpost in sidecar_to_children_list:
        thissubnode = thissubpost.get('node',{})
        if thissubnode:
          subdisplayurl = thissubnode.get('display_url')
          thatpost = {}
          thatpost['display_url'] = subdisplayurl
          sidecar_to_children_list.append(thatpost)
  return thispost

def list_links_from_response_hash(response_hash):
#  time.sleep(1)
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
    thispost = node
    # thispost will be a hash
    post_object = process_post(thispost)
    thispost = post_object
#    dimensions = thispost.get('dimensions',{})
#    if dimensions:
#      height = dimensions.get('height','')
#      width = dimensions.get('width','')
#    display_url = thispost.get('display_url','')
#    is_video = thispost.get('is_video',False)
#    tagged_user_list = thispost.get('edge_media_to_tagged_user',[])
#    accessibility_caption = thispost.get('accessibility_caption','')
#    caption = ''
#    if node.get('edge_media_to_caption',''):
#      captionlist = node['edge_media_to_caption']['edges']
#      if captionlist:
#        caption = captionlist[0]
#    userid = ''
#    username = ''
#    owner = node.get('owner',{})
#    if owner:
#      userid = owner.get('id','')
#      username = owner.get('username','')
#    location = thispost.get('location','')
#    posts_beyond_first = []
#    sidecar_to_children_list = []
#    sidecar_to_children = thispost.get('edge_sidecar_to_children',{})
#    if sidecar_to_children:
#      sidecar_to_children_list = sidecar_to_children.get('edge',[])
#      if sidecar_to_children_list:
#        for thissubpost in sidecar_to_children_list:
#          thissubnode = thissubpost.get('node',{})
#          if thissubnode:
#            subdisplayurl = thissubnode.get('display_url')
#            thatpost = {}
#            thatpost['display_url'] = subdisplayurl
#            sidecar_to_children_list.append(thatpost)
#    batch_list.append(display_url)
    batch_list.append(thispost['display_url'])
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

def get_next_response_hash(doc_id,user_id,end_cursor,num,sessionid):
  if end_cursor:
    request_url = 'https://www.instagram.com/graphql/query/?doc_id=' + doc_id + '&variables=%7B%22id%22%3A%22' + user_id + '%22%2C%22after%22%3A%22' + end_cursor + '%22%2C%22first%22%3A' + num + '%7D'
    header_hash = {
    }
    header_hash['Cookie'] = 'sessionid=' + sessionid + '; ds_user_id=CAFE'
    header_hash['x-ig-app-id'] = app_id
    headers = header_hash
    response = requests.get(request_url, headers=headers)
    response_hash = json.loads(response.text)
    return response_hash

app_id = get_app_id(username)
response_hash = get_first_set(username,app_id,sessionid)
print_links_from_response_hash(response_hash)
this_list = list_links_from_response_hash(response_hash)
all_photos_list = all_photos_list + this_list

# hard-coded, hopefully always the same
doc_id = '17991233890457762'
user_id = get_user_id_from_response_hash(response_hash)
end_cursor = get_end_cursor_from_response_hash(response_hash)
num = '50'

while end_cursor:
  next_response_hash = get_next_response_hash(doc_id,user_id,end_cursor,num,sessionid)
  print_links_from_response_hash(next_response_hash)
  this_list = list_links_from_response_hash(next_response_hash)
  all_photos_list = all_photos_list + this_list
  doc_id = '17991233890457762'
  user_id = user_id
  end_cursor = get_end_cursor_from_response_hash(next_response_hash)
  num = '50'
  print('!!!!!!!!!!!!!!!')

print('GROOGROOGROOGROOGROOGROOGROO')
print(json.dumps(all_photos_list))
outfilename = 'all_photos_list3.json'
thisoutfile = open(outfilename, 'w')
thisoutfile.write(json.dumps(all_photos_list))
