import hashlib
#this goes in util

myfile = open("data/login.csv", "r")
m = myfile.read()
m = m.split("\n")
m = m[0: len(m) - 1]
d = dict()
for line in m:
    l = line.split(',')
    d[l[0]] = l[1]
myfile.close()

def add(k, i):
  if k in d.keys():
    return "USERNAME TAKEN"
  h = hashlib.sha1(i).hexdigest()
  myfile = open("data/login.csv", "a")
  myfile.write(k + "," + h + "\n")
  myfile.close()
  return "SUCCESS"

def check(k, i):
  h = hashlib.sha1(i).hexdigest()
  if k in d.keys():
    print d[k]
    print h
    if d[k] == h: return True
  return False
