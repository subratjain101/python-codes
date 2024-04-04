
names = ("Krishna", "Balram", "Subadhra", "Rukmini")
ages = (15, 15, 14, 14)

person_info = zip(names, ages)
person_info = tuple(person_info)

for i in range(len(person_info)):
    name, age = person_info[i]
    print(f"Name: {name}, age: {age}")
