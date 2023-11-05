import requests
import re
import shutil

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
#      print('***************')
      header_value = header_pair[0][1]
#      print(header_name)
#      print(header_value)
#      print('---------------')
      header_hash[header_name] = header_value


source = 'https://scontent-iad3-2.cdninstagram.com/v/t51.2885-15/28428546_1859314474081035_8429563154572247040_n.jpg?stp=dst-jpg_e35&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=103&_nc_ohc=QoZGlxlD4RkAX8PekQy&edm=APU89FABAAAA&ccb=7-5&oh=00_AfAUFaKPbEwhQa-TSgE_aVp9LhEZ6rVIPsiLaL4rWaUhTA&oe=654C34BF&_nc_sid=bc0c2c'
filename = 'myphoto.jpg'

def download_single_photo(source,filename):
  source = source
  photo_filename = filename
  url_response = requests.get(source, stream=True)
  with open(photo_filename, 'wb') as out_file:
    shutil.copyfileobj(url_response.raw, out_file)

##headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0'}
#headers = header_hash
 
#response = requests.get(request_url, headers=headers)

#print(response.text)

download_single_photo(source,filename)
