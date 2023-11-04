import requests
import re
import json

#request_url = 'https://www.instagram.com/api/v1/users/web_profile_info/?username=vintage_bmore_graffiti'
username = 'vintage_bmore_graffiti'

def get_app_id(username):
  request_url = 'https://www.instagram.com/' + username + '/'

  headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0'}
 
  proxies = {}
#  proxies = {
#    'http' : 'http://localhost:8888',
#    'https' : 'http://localhost:8888',
#  }
  response = requests.get(request_url, headers=headers, proxies=proxies, verify=False)
  raw_html = response.text
#  print(raw_html)
#  useridhits = re.findall(r"\"profile_id\":\"(.*?)\"",raw_html)
#  useridhits = re.findall(r"(.*)",raw_html)
#  userid = useridhits
#  print(userid)

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
#        print(appid)
        return app_id

app_id = get_app_id(username)
print(app_id)

request_url = 'https://www.instagram.com/api/v1/users/web_profile_info/?username=cannibal_corpse_limericks'
header_hash = {}
header_hash['x-ig-app-id'] = '936619743392459'
headers = header_hash
response = requests.get(request_url, headers=headers)
#print(response.text)

response_hash = json.loads(response.text)

data = response_hash['data']
user = data['user']
edge_owner_to_timeline_media = user['edge_owner_to_timeline_media']
edges = edge_owner_to_timeline_media['edges']

# this drills down and prints links to the full image for the top twelve results for this user
# only works for public since not using authentication
for thisedge in edges:
  node = thisedge['node']
  display_url = node['display_url']
  print(display_url)
