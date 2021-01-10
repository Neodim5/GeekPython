import json

with open('person.json') as file_stream:
    person = json.load(file_stream)
    print(sum(person['salaries']))


