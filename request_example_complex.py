import requests
import re

file = 'curlcmd.txt'
header_hash = {}
with open(file) as fd:
  lines = fd.read().splitlines()
  for thisline in lines:
    curl_command = thisline
    headers = re.findall(r"-H\s+\"([^\"]*)\"",thisline)
    for thisheader in headers:
      header_pair = re.findall(r"^(.*?):\s*(.*)$",thisheader)
      header_name = header_pair[0][0]
      print('***************')
      header_value = header_pair[0][1]
      print(header_name)
      print(header_value)
      print('---------------')
      header_hash[header_name] = header_value

request_url = 'https://www.instagram.com/api/v1/users/web_profile_info/?username=vintage_bmore_graffiti'

#headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0'}
headers = header_hash
 
response = requests.get(request_url, headers=headers)

print(response.text)
