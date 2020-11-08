#Function is a block of code which only runs when called. In Py, we do not use curly's, we use indentation with tabs or spaces

#Create function

def sayHello(name):
    print(f'Hello {name}')

sayHello('John Doe')

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total


num = (getSum(3,4))

print(num)



# A lamba function is a small anonymous function
# A lamdba function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions.

getSum = lambda num1, num2 : num1 + num2

print(getSum(10, 3))


