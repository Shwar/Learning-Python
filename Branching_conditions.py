# Loops and if else statements and comparison statements

#Comparison operators compares values or operands then produce a boolean value on a condition

#Strings can be compared too and equality operator is case sensitive

print('a' == 'A') #False

#if statement

age = 17
if age >18:
    print('You are eligible')
else:
    print('Inelligible') 
print("Move on")  

#Loops
# Range function outputs oan ordered sequence as list, If the input is positive integer, the output is sequence

#Sequence contins same number of elements but starts at zero
#If range fun has two values, the first input is smaller thaan seconfd ,output is a sequence that starts at first input then iterates up to not including second input
x =range(0,3) # outputs 0,1,2

for n in x:
    print(n)

y =range(2) #Output 0,1
for z in y:
    print(z)

#for loop
seq = [1,2,3,4]

for i in range(0,5):
    print(i)

     
#While loop
 # Code to be executed while the condition is true
    # Indentation is crucial to indicate the scope of the loop

    num = 1

    while num <= 10:
        print(num)
        num+=1

        #The while loop is used to repeatedly execute a block of code as long as a given condition is True. In this case, the condition is count <= 10,
        # meaning the loop will continue as long as count is less than or equal to 10.

       
       
        #We use for loop when we are sure  of the iterations and length and while loop is used when we want to print valuesa s long as condition given is true


        # Try for catching error in python
        try: 
            num = int(input("Enter a number: ")) 
        except ValueError: 
            print("Invalid input. Please enter a valid number") 
        else: 
            print("You entered:", num)

            # try: # Code that might raise an exception except 
        #ExceptionType: # Code to handle the exception 
        #finally: # Code that always executes regardless whether an exception occurs