import re

file = 'curlcmd.txt'
with open(file) as fd:
  lines = fd.read().splitlines()
  for thisline in lines:
    curl_command = thisline
    headers = re.findall(r"-H\s+\"([^\"]*)\"",thisline)
    for thisheader in headers:
      print(thisheader)

