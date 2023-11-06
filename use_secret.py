import mysecret

print('hello')
secret = mysecret.Mysecret()
print(secret.userid)
print(secret.password)
print(secret.sid)
secret.blah = 'FAKEBLAH'
print(secret.blah)
