#JSON is commonly used with data APIs/. HEre's how you can parse JSON into a python dict

import json

#Sample JSON

userJSON = '{"first_name": "John", "last_name": "Doe", "age": "30"}'

# Parse to dictionary

user = json.loads(userJSON)
# print(user)

# print(user['first_name'])

# Dictionary to JSON format

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)

print(carJSON)