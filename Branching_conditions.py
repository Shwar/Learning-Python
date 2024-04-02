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
    print(seq[i] = 3)
     

