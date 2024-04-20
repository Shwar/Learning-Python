# We use open functions



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
# We cab use for to iterate through each line

with open("Example.txt","r") as file2:
    for line in file2:
        print(line)
   
    
  

with open("Example.txt","r") as file:
  
    #Can use method readline() to read the first line or specific indexes
    content = file.readline()
    print(content)

    content = file.readline(4)
    print(content)

   

