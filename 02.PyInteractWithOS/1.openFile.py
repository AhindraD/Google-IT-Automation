file = open("read.txt")
print(file.readline())  # reads the first line
print(file.readline())  # reads the second line
print(file.read())  # reads the rest of the file
file.close()  # necessary


# python takes care of closing the file if we use with
with open("read.txt") as file:
    print(file.read())
# auto file closed