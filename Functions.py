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
    return f'Good mornning {name}. How was your weekend {name}'

for i in range(3):
    print(say_hi("Alice"))


class PersonAccount:
    def __init__(self,firstname ='John',lastname='Doe' , salary=700000, commission=120000, allowance=60000, fees=10000, food=200000, insurance=20000, transport=50000, rent=250000):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.commission = commission
        self.allowance = allowance
        self.rent = rent
        self.fees = fees
        self.food = food
        self.insurance = insurance
        self.transport = transport
        
        
    def total_income(self):
        return self.allowance + self.commission +  self.salary
       
    
    def total_expenses(self):
       
        return self.transport + self.fees + self.food + self.insurance + self.rent
    def account_balance(self):
        return  self.total_income() - self.total_expenses()
       
    
    def acc_info(self):
        return f'Dear {self.firstname} {self.lastname} your total income is {self.total_income()}. Your expenses totals up to {self.total_expenses()}. Your remaining balance is {self.account_balance()}'
    
    
    

acc1 = PersonAccount('James','Tarkowski', 350000, 200000,150000, 50000,90000,2000,20000,60000)

print(acc1.acc_info())
print(acc1.total_expenses())
print(acc1.total_income())

acc2 = PersonAccount()
print(acc2.acc_info())



import statistics
data = []
maximum = max(data)
minimum = min(data)

class Statistics:
    def __init__(self,data):
        self.data = data

    def Count(self):
        return data.count(data)
    def mean(self):
        return statistics.mean(data)
    def median(self):
        return statistics.median(data)
    def range(self):
        return maximum - minimum
    def std_dev(self):
        return statistics.stdev(data)
    def var(self):
        return statistics.variance(data)
    def mode(self):
        return statistics.mode(data)
    

    def describe(self):
        print(f'Count:{self.Count()}')
        print(f'Mean:{self.mean()}')
        print(f'Median:{self.median()}')
        print(f'Range:{self.range()}')
        print(f'Std deviation:{self.std_dev()}')
        print(f'Variance:{self.var()}')
        print(f'Mode:{self.mode()}')

stat1 = Statistics([20,30,40,50,60])
print(stat1.describe())
