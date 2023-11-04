import requests
import re
import json

# UPDATE : I think the only header that is necessary is the x-ig-app-id header 
# which may always be equal to 936619743392459

file = 'curlcmd.txt'
header_hash = {}
header_hash['x-ig-app-id'] = '936619743392459'
with open(file) as fd:
  lines = fd.read().splitlines()
  for thisline in lines:
    curl_command = thisline
    headers = re.findall(r"-H\s+\"([^\"]*)\"",thisline)
    for thisheader in headers:
      header_pair = re.findall(r"^(.*?):\s*(.*)$",thisheader)
      header_name = header_pair[0][0]
#      print('***************')
      header_value = header_pair[0][1]
#      print(header_name)
#      print(header_value)
#      print('---------------')
#      header_hash[header_name] = header_value
      #header_hash['x-ig-app-id'] = '936619743392459'
#request_url = 'https://www.instagram.com/api/v1/users/web_profile_info/?username=vintage_bmore_graffiti'
request_url = 'https://www.instagram.com/api/v1/users/web_profile_info/?username=cannibal_corpse_limericks'

#headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0'}
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
