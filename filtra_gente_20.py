people = [
    {
        "name":"Edgar",
        "age":31
        },
    {
        "name":"Alan",
        "age":18
        },
    {
        "name":"Adan",
        "age":20
        }
    ]

people_20 = []
for i in people:
     if i["age"]==20:
         people_20.append(i)


print(people_20)
