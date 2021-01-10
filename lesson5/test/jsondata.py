import json

person = {
    "name": "Dmitry",
    "age": 40,
    "salaries": [100, 200, 150]
}
with open('person.json', 'w') as file_stream:
    json.dump(person, file_stream)

