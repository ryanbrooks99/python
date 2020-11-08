#IF/ELSE conditions used to decide to do something based on something being true or false.

x = 20
y = 20

# Comparison Operators (==, !=, <, >, >=, <=) - used to compare values

# #Simple if
# if x > y :
#     print(f'{x} is greater than {y}')

# #If else
# if x > y :
#     print(f'{x} is greater than {y}')
# else:
#     print(f'{y} is greater than {x}')


#ELIF
# if x > y :
#     print(f'{x} is greater than {y}')
# elif  x == y:
#     print(f'{x} is equal to {y}')
# else:
#     print(f'{y} is greater than {x}')

# Nested if
# if x > 2:
#     if x <= 10:
#         print(f'{x} is greater than 2 or less than or equal to 10')




# #Logical operators (and, or, not) - Used to combined conditional statements

# if x > 2 and x <= 10:
#         print(f'{x} is greater than 2 or less than or equal to 10')

# if x > 2 or x <= 10:
#         print(f'{x} is greater than 2 or less than or equal to 10')

# if not(x == y):
#         print(f'{x} is not equal to {y}')


#Membership Operator (Not, Not In)- membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]

# #IN
# if x in numbers:
#     print(x in numbers)

# #NOT IN
# if x not in numbers:
#     print(x not in numbers)



#Identity Operators
if x is y:
    print(x is y)