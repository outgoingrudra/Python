people = [
    {"name": "Ravi", "age": 25},
    {"name": "Anita", "age": 22},
    {"name": "Ravi", "age": 20}
]
sorted_people = sorted(people, key=lambda x: (x["name"], x["age"]))
print(sorted_people)
