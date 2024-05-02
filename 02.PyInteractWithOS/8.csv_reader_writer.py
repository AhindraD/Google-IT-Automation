import csv

readF = open("csv_data.txt")
csv_f = csv.reader(readF)
list_f = []
for row in csv_f:
    print(row)
    name, phone, role = row
    list_f.append(row)
    print(f"Name: {name:.>6}, Phone: {phone}, Role: {role}")
readF.close()

with open("hosts.csv", "w") as writeF:
    csv_w = csv.writer(writeF)
    csv_w.writerows(list_f)
