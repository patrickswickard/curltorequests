import requests
import re
import json
import shutil
import time

# method to download a single photo, takes url as source and dl target as filename
def download_single_photo(source,filename):
  source = source
  photo_filename = filename
  url_response = requests.get(source, stream=True)
  with open(photo_filename, 'wb') as out_file:
    shutil.copyfileobj(url_response.raw, out_file)

all_photo_list = []
file = 'cache/all_photos_list.json'
with open(file) as fd:
  lines = fd.read().splitlines()
  for thisline in lines:
    all_photo_list = json.loads(thisline)

print(all_photo_list)

count = 0
for thisphotolink in all_photo_list:
  count += 1
  if count <= 9:
    countpad = '000'
  elif count <= 99:
    countpad = '00'
  elif count <= 999:
    countpad = '0'
  else:
    countpad = ''
  print(thisphotolink)
  print(str(count))
  outfilename = 'cache/photo_dftm_' + countpad + str(count) + '.jpg'
  print(outfilename)
  print('Downloading')
  time.sleep(1)
  download_single_photo(thisphotolink,outfilename)
