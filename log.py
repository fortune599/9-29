import hashlib
#this goes in util

def log(k, i):
  h = hashlib.sha1(i).hexdigest()
  myfile = open("log.csv", "a")
  myfile.write(k + "," + h + "\n")
  myfile.close()
  return;

def check(k, i):
  h = hashlib.sha1(i).hexdigest()
  myfile = open("log.csv", "r")
  m = myfile.readlines()
  l = []
  for line in m:
    l = line.split(',')
    if (l[0] == k && l[1] == h):
      return true;
  return false;
