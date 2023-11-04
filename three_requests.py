import requests
import re
import json

#request_url = 'https://www.instagram.com/api/v1/users/web_profile_info/?username=vintage_bmore_graffiti'
#username = 'vintage_bmore_graffiti'
username = 'cannibal_corpse_limericks'

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

request_url = 'https://www.instagram.com/api/v1/users/web_profile_info/?username=' + username
header_hash = {}
#header_hash['x-ig-app-id'] = '936619743392459'
header_hash['x-ig-app-id'] = app_id
headers = header_hash
response = requests.get(request_url, headers=headers)
#print(response.text)

response_hash = json.loads(response.text)

data = response_hash['data']
user = data['user']
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

# hard-coded, hopefully always the same
# okay maybe not - if I replace cancorp then this gives me next items for vintage graf
doc_id = '17991233890457762'
num = '100'

if end_cursor:
  #request_url = 'https://www.instagram.com/graphql/query/?doc_id=17991233890457762&variables=%7B%22id%22%3A%2261247467864%22%2C%22after%22%3A%22QVFDNlR2SFNibHlyR1VjekYxejdHeERVYWcxekhmWHZ5ZWJtY2JBa1dQMWpwYURkb0xFVDlncEZ2U1VZTEZrMXM0bHBBZ3UwQlhZSTZlWV9oVlJXRFN5dQ%3D%3D%22%2C%22first%22%3A12%7D'
  request_url = 'https://www.instagram.com/graphql/query/?doc_id=' + doc_id + '&variables=%7B%22id%22%3A%2261247467864%22%2C%22after%22%3A%22' + end_cursor + '%22%2C%22first%22%3A' + num + '%7D'
  header_hash = {}
  #header_hash['x-ig-app-id'] = '936619743392459'
  header_hash['x-ig-app-id'] = app_id
  headers = header_hash
  response = requests.get(request_url, headers=headers)
  response_hash = json.loads(response.text)
  print(response.text)

print('***************')
print(end_cursor)


print('!!!!!!!!!!!!!!!!!!!!!')
data = response_hash['data']
user = data['user']
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
