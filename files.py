#Python has functions for CRUD files

#Open a file

myFile = open('My File.txt', 'w')

#Get info on file
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

myFile.write('I love Python')
myFile.write(' And Javascript')
myFile.close()

#Append to file
myFile = open('My File.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

#Read from file
myFile = open('My File.txt', 'r+')
text = myFile.read(100)
print(text)