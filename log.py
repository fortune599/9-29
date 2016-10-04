import hashlib

#this goes in util
def log(k, i):
  h = hashlib.sha1(i)
  myfile = open("log.csv", "a")
  myfile.write(k + "," + h.hexdigest() + "\n")
  myfile.close()
  return;
