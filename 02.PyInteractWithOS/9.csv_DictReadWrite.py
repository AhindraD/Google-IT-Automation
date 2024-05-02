import csv
with open("software.csv") as s_file:
    reader = csv.DictReader(s_file)
    for row in reader:
        print(row)
        print(f"{row["name"]} has {row["users"]} users")


# DictWriter
users = [
    {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
    {"name": "Lio Nelson", "username": "lion",
        "department": "User Experience Research"},
    {"name": "Charlie Grey", "username": "greyc", "department": "Development"}
]
keys = ["name", "username", "department"]
with open("by_department.csv","w") as d_file:
    writer=csv.DictWriter(d_file,fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)