# a list is a collection which is ordered and changeable. Allows duplicate members.


# Create list

numbers = [1,2,3,4,5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

#Constructor
# numbers2 = list((1,2,3,4,5))

#get value
print(fruits[1])

#get length
print(len(fruits))

#remove from list
fruits.remove('Grapes')

# Insert into new postition
fruits.insert(2, 'Strawberries')

#Remove witrh pop
fruits.pop(2)

#Reverse
fruits.reverse()

#Sort alpha
fruits.sort()

#Change value
fruits[0] = "Blueberries"


print(fruits)