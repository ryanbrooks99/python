# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#Creat dict

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

#Constructor

# person2 = dict(first_name='Sarah', last_name="Williams")

#Get value

print(person['first_name'])
print(person.get('last_name'))

#Add key value
person['phone'] = '555-555-5555'

#Get dict keys
print(person.keys())


#Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

#Remove item

del person['age']
person.pop('phone')

person.clear()

print(person)

#List of dictionaries

people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])