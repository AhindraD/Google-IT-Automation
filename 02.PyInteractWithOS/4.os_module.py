import os
import datetime

print(os.path.exists("written.txt"))
print(os.path.getsize("written.txt"))


#get last modified timestamp
timestamp = os.path.getmtime("written.txt")
print(datetime.datetime.fromtimestamp(timestamp))
#make the unix timestamp readable


#get absolute path of the file
absPath=os.path.abspath("written.txt")
print(absPath)


#get current working directory
print(os.getcwd())
# os.mkdir("newDir")
os.chdir("newDir")#change directory
print(os.getcwd())