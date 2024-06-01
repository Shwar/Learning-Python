"""
stackSize = ['James', 'Mark',1,2]
maxSize = 4

def isEmpty():
    length = len(stackSize)
    if length ==0:
        print("Stack is empty")
    else:
        print(f"Stack has items {stackSize}")    

def addEStacklement(x):
    if len(stackSize) <= maxSize:
        stackSize.append(x)
        print(stackSize)
    else:
        print("Stack is full  cannot append an item!")    

def deleteStack():
    if len(stackSize) == 0:
        print("Stack is already empty!")
        print(stackSize)    

    else:
        stackSize.pop()
        print(stackSize)   
def checkTopItem():
    top = stackSize[0] 
    print("The top item in the stack is " +top)
       
        
isEmpty()
deleteStack()
addEStacklement(6)
deleteStack()
addEStacklement(6)
deleteStack()
deleteStack()
checkTopItem()

"""


class stackOperation:
    stackSize = ['James', 'Mark',1,2]
    length = len(stackSize)
    top = stackSize[0]


    def __init__(self, maxSize=4):
        self.maxSize = maxSize
    def isEmpty(self):
        if self.length == 0:
            print("Stack is empty!")

        else:
            print(f"Stack has this elements{self.stackSize}")  

    def addStackElement(self, x):
        self.x = x
        if self.length <= self.maxSize:
            self.stackSize.append(self.x)
            print(self.stackSize) 
        else:
            print("The stack is full cannot append an item!")

    def deleteStackItem(self):
        if self.length == 0:
            print("Stack is already empty!")
            print(self.stackSize)

        else:
            self.stackSize.pop()
            print(self.stackSize)  

    def checkTopItem(self):
        print(f"The top item is {self.top}")

        
stack1 = stackOperation()
stack1.isEmpty()
stack1.addStackElement(8)
stack1.deleteStackItem()
stack1.checkTopItem()
        