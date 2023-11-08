import requests
import re
import json
import mysecret

#username = 'vintage_bmore_graffiti'
#username = 'cannibal_corpse_limericks'
username = 'bugbobbie'
username = 'dont_fear_the_millimeter'

secret = mysecret.Mysecret()
sessionid = secret.sid
print(sessionid)

def get_app_id(username):
  debug = True
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

app_id = get_app_id(username)
print(app_id)
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
  #print(response.text)
  response_hash = json.loads(response.text)
  return response_hash

def print_links_from_response_hash(response_hash):
  data = response_hash['data']
  user = data['user']
  #user_id = user['id']
  edge_owner_to_timeline_media = user['edge_owner_to_timeline_media']
  page_info = edge_owner_to_timeline_media['page_info']
  edges = edge_owner_to_timeline_media['edges']
  has_next_page = page_info['has_next_page']
  end_cursor = ''
  if has_next_page:
    end_cursor = page_info['end_cursor']

  # this drills down and prints links to the full image for the top twelve results for this user
  # only works for public since not using authentication
  for thisedge in edges:
    node = thisedge['node']
    display_url = node['display_url']
    print(display_url)

print('-----------------------')

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

response_hash = get_first_set(username,app_id)

print('HELLO')
print(response_hash)
print('HI')

# hard-coded, hopefully always the same
doc_id = '17991233890457762'
user_id = get_user_id_from_response_hash(response_hash)
end_cursor = get_end_cursor_from_response_hash(response_hash)
num = '50'

def get_next_response_hash(doc_id,user_id,end_cursor,num,sessionid):
  if end_cursor:
    request_url = 'https://www.instagram.com/graphql/query/?doc_id=' + doc_id + '&variables=%7B%22id%22%3A%22' + user_id + '%22%2C%22after%22%3A%22' + end_cursor + '%22%2C%22first%22%3A' + num + '%7D'
    header_hash = {
    }
    #header_hash['x-ig-app-id'] = '936619743392459'
    # OBOE sessionid pos 1, steal a fresh one
    header_hash['Cookie'] = 'sessionid=' + sessionid + '; ds_user_id=CAFE'
    header_hash['x-ig-app-id'] = app_id
    headers = header_hash
    response = requests.get(request_url, headers=headers)
    response_hash = json.loads(response.text)
    return response_hash

next_response_hash = get_next_response_hash(doc_id,user_id,end_cursor,num)

print('!!!!!!!!!!!!!!!!!!!!!')

print_links_from_response_hash(next_response_hash)
