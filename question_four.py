
#SECTION C

# 4 (i) a) Object-oriented programming is a computer programming model that 
# organizes software around objects, or data fields, instead of logic and functions
#it helps create applications that are maintainable, scalable, and robust

#b) In object-oriented programming (OOP), a class is a template for creating objects. 
# while an object is an instance of a class


#4(ii)python program that counts the occurrances of each word.??


#4(iii) Python function that takes 2 parameters (a and b) & returns their sum
#Defining a functon
def sum_numbers(a,b):
    return a + b

#testing the function with a=3 and b=4
results = sum_numbers(3 , 4)

print('The sum of a and b is:',results)



#4(iv)
# Define the Car class
class Car:
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name
        self.color = color

# Instantiating an object of the Car class

personal_car = Car(brand = "Toyota", name = "Hammer", color = "Red")

# Printing the attributes of the Car object

print("The Car Brand is: ", personal_car.brand)
print("The Car Name is: ", personal_car.name)
print("The Car Color is: ", personal_car.color)



#4(v) start_engine  Method to the Car class

class Car:
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name
        self.color = color

# Method to start the engine

    def start_engine(self):
        print(f"The engine of the {self.brand} {self.name} has started.")

personal_car = Car(brand="Toyota", name="Hammer", color="Red")

# Calling the start_engine method
personal_car.start_engine()
