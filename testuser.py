import requests
import re
import json
import shutil
import mysecret
import time
import instapost

username = 'bugbobbie'
secret = mysecret.Mysecret()
sessionid = secret.sid

my_user = instapost.Instauser()

print(my_user.dumps())
