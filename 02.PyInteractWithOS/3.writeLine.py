with open("written.txt", "w") as file:
    file.write("Hello\n")
    file.write("World\n")

with open("written.txt", "a") as file:
    file.write("Hii\n\t")
    file.write("Yaaa!\n")
