# We use open functions

 #It takes two primary parameters:

#File path: The file path parameter consists of the filename and directory where the file is located.

#Mode: The mode parameter specifies the purpose of opening the file, such as 'r' for reading, 'w' for writing, or 'a' for appending.

# Using the read method, you can retrieve the complete content of a file
file1 = open("Example.txt", "r")
print(file1)

print(file1.closed)

# Method close() used to close the object - Always close the object
file1.close()

print(file1.closed)

# The methods .name and .mode gets name and mode of the file
print(file1.mode)
print(file1.name)


# To do away with close() all the time we use with
#advantages of using the 'with' statement are:

#Automatic resource management: The file is guaranteed to be closed when you exit the with block, even if an exception occurs during processing.
#Cleaner and more concise code: You don't need to explicitly call close(), making your code more readable and less error-prone.

# We can use for to iterate through each line

with open("Example.txt","r") as file2:
    for line in file2:
        print(line)
   
    
  

with open("Example.txt","r") as file:
  
    #Can use method readline() to read the contents of yhe file line by line and store it in a list
    content = file.readline(4)
    print(content)

#It can be called multiple times to read subsequent lines.
    content = file.readline(10)
    print(content)

#Looping through lines: Typically, you use a while loop to read lines until no more lines are left 
while True:
    line = file2.readline()
    if not line:
        break
    print(line)
    

