
#A class is a blueprint for creating objects. It define objects structure
#We create using class keyword. Assign attributes(data) and methods which we define as functions()
#An object is a fundamental unit in Python that represents a real-world entity or concept.
#Objects can be tangible (like a car) or abstract (like a student's grade).

# Objects has state and behaviours as characteristics

#State or attributes include color, speed
#Behaviour or methods include accelerate

#Class attributes are variables shared among all class instances (objects). In below code tyhe max_speed




class MyCar:

    # Class attributes (shared by all instances)
    max_speed=120

    # Constructor method (initialize instance attributes)
    def __init__(self,make,model,color,speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed

    def accelerate(self, acceleration):
        if self.speed + acceleration <= MyCar.max_speed:
            self.speed+=acceleration

        else:
            self.speed = MyCar.max_speed


    def get_speed(self):
        return self.speed
    
#To create objects (instances) of the class, you call the class like a function and provide arguments the constructor requires.
car1 = MyCar("Honda","Civic","Silver")
car2 = MyCar("Toyota", "Camry", "Blue")

car1.accelerate(20)
car2.accelerate(30)

print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h.")
print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h.")

class circle:

 def __init__(self,radius,color):
        self.radius = radius
        self.color = color

def addRadius(self, r):
        self.radius = self.radius +r  

def drawCircle(self):
        pass

RedCircle = circle(10,"Red")   

drawCircle(RedCircle)





        



         