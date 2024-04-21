# We use open functions

 #It takes two primary parameters:

#File path: The file path parameter consists of the filename and directory where the file is located.

#Mode: The mode parameter specifies the purpose of opening the file, such as 'r' for reading, 'w' for writing, or 'a' for appending.

# Using the read method, you can retrieve the complete content of a file
"""
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
    
"""
    #Writing files

with open("Example2.txt", "w") as file3:
        file3.write("Line A\n")
        file3.write("Line B")

# Using a for loop
lines = "Line A1\n", "Line A2\n", "Line A3\n"

with open("Example3.txt", "w") as file4:
        for line in lines:
                file4.write(line)


# We use append method to use existing file instead of creating new

with open("Example3.txt", "a") as file5:
        file5.write("This is line 4")


# We can copy a file to another file

# Open the source file for reading
with open("Example3.txt", "r") as readfile:
        
        # Open the destination file for writing
        with open("Example4.txt","w") as writefile:
                
                 # Read lines from the source file and copy them to the destination file one by one
                for line in readfile:
                        writefile.write(line + "\n")      


new_line = "This is a new line"     

with open("Example4.txt","a") as file5:
        file5.write(new_line)

 # We can use mode 'a+' to append and read        

with open("Example4.txt", "a+") as file6:
        file6.write("This is line E \n")        