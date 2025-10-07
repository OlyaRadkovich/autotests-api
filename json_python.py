import json

json_data = '{"name": "Petro", "age": 31, "is_student": false, "courses": ["Python", "Java", "CI/CD"]}'
parsed_json = json.loads(json_data)
print(parsed_json["courses"][0])

dict_data = {
    'name': 'Жека',
    'age': 38,
    'is_student': False
}

json_string = json.dumps(dict_data, indent=4)
print(json_string)

with open("json_example.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data)

with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(dict_data, file, indent=2, ensure_ascii=False)
    print(dict_data)