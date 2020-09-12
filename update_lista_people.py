people = [
    {
        "name":"Edgar",
        "age":31
        },
    {
        "name":"Alan",
        "age":18
        }
    ]

salary = [
    {
        "name":"Edgar",
        "salary":50000.00
        },
    {
        "name":"Alan",
        "salary":30000.00
        }
    ]

for index,i in enumerate(people):
    if i["name"] == salary[index]["name"]:
       i["salary"] = salary[index]["salary"]

print(people)
