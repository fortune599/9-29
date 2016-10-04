import hashlib
#this goes in util

myfile = open("log.csv", "r")
m = myfile.readlines()
myfile.close()
d = dict()
for line in m:
    d[line.split(',')[0]] = line.split(',')[1]

def log(k, i):
  if k in d.keys():
    return "USERNAME TAKEN"
  h = hashlib.sha1(i).hexdigest()
  myfile = open("log.csv", "a")
  myfile.write(k + "," + h + "\n")
  myfile.close()
  return "SUCCESS"

def check(k, i):
  h = hashlib.sha1(i).hexdigest()
  if k in d:
    if d[k] == h: return True
  return False
