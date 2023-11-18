import requests
import re
import json
import shutil
import mysecret
import time
import instatools

username = 'bugbobbie'
secret = mysecret.Mysecret()
sessionid = secret.sid

my_user = instatools.Instauser()
my_user.get_user_from_web(username,sessionid)

print(my_user.dumps())
