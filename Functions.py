#Functions take inputs and produce ouputs
#Functions are reusable piece of code - functions promote code modularity,debugging , readability,abstraction, collaboration and maintainennace

#Defined with keyword def and takes parameters/arguments 
def add1(input):
    output=input+1
    return output

#we call function with its name and parenthesis and its parameters

print(add1(5))

#There are built in functions  like len(), sum(), max(), min(), and sorted()
items = (1,2,9,6,4,3)
print(max(items))
print(min(items))
print(sorted(items))
print(sum(items))


#"pass" statement in a programming function is a placeholder or a no-op (no operation) statement.
# Use it when you want to define a function or a code block syntactically but do not want to specify any functionality or implementation at that moment.
def passFun():
   pass

#Docstrings explain what a function does
#Placed inside triple quotes under the function definition 

def mult(a,b):
    """
    This function takes two parameters and multiply them and return a value
    """
    return a * b

print(mult(3,4))

#Global Scope: Variables defined outside functions; accessible everywhere
#Local Scope: Variables inside functions; only usable within that function

def varibales():
    local_var = "I am a local  variable"
    return local_var

global_var = "I am a global variaable"

print(global_var)
print(varibales())
 #print(local_var) #Outputs an error 'local_var' not defined

#Functions can contain code with loops
#This makes complex tasks more organized
#The loop code becomes a repeatable function

def print_numbers(limit):
    for i in range (limit+1):
        print (i)
    
print_numbers(5)

def say_hi(name):
    return "Hello: "+name

for i in range(3):
    print(say_hi("Alice"))
