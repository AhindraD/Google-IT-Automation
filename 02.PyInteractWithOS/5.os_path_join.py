import os

dir = "website"
# lists files and directories in directory
for name in os.listdir(dir):
    # concats path - os independent
    fullname = os.path.join(dir, name)
    # checks if it is a directory or file
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
