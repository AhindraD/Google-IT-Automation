with open("read.txt") as file:
    for line in file:
        print(line.strip().upper())


file=open("read.txt")
lines=file.readlines()#returns list
lines.sort()#sorts the list alphabetically
file.close()
print(lines)