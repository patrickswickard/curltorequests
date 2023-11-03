import requests
import re
import json

#request_url = 'https://www.instagram.com/api/v1/users/web_profile_info/?username=vintage_bmore_graffiti'
username = 'vintage_bmore_graffiti'
request_url = 'https://www.instagram.com/' + username + '/'

#headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0'}
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0'}
 
#proxies = {}
proxies = {
  'http' : 'http://localhost:8888',
  'https' : 'http://localhost:8888',
}
response = requests.get(request_url, headers=headers, proxies=proxies, verify=False)
raw_html = response.text
print(raw_html)
#useridhits = re.findall(r"\"profile_id\":\"(.*?)\"",raw_html)
#useridhits = re.findall(r"(.*)",raw_html)
#userid = useridhits
#print(userid)

responselines = response.text.splitlines()

for thisline in responselines:
  hit = re.search(r"APP_ID",thisline)
  if hit:
    jsonthisline = re.findall(r"<script[^>]*>\s*(.*?)\s*</script>",thisline)
    if jsonthisline:
      jsontext = jsonthisline[0]
      # this json is so disorganized it's not even worth parsing
      #thishash = json.loads(jsontext)
      appidhits = re.findall(r"\"APP_ID\":\"(.*?)\"",jsontext)
      appid = appidhits[0]
#      useridhits = re.findall(r"\"profile_id\":\"(.*?)\"",raw_html)
#      useridhits = re.findall(r"(.*)",raw_html)
#      userid = useridhits
      print(appid)
#      print(userid)
