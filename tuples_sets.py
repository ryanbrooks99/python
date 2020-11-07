# Tuple is a collection which is ordered and unchanegable. Allows duplicate members


#Create tuple

fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

#Single value need a trailing comma
fruits2 = ('Apples',)

#Delte tuple
del fruits2

# print(len(fruits2))

# fruits[0] = 'Pears'


# A set is a collection which is unordered and unindexed. No duplicate members


# Create set

fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in a set
print('Apples' in fruits_set)

#Add to set
fruits_set.add('Grape')

#Remove from set
fruits_set.remove("Grape")

#Clear set
fruits_set.clear()

print(fruits_set)
