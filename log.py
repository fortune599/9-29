import hashlib

#this goes in util
def log(k, i):
  myfile = open("log.csv", "a")
  myfile.write(k + "," + i + "\n")
  myfile.close()
  return;
