#Kayla Allinger
#CaseStudyListsAndFunctions.py
#This program will accept user input for a car, store the attributes and then
#output the data in an easy to read format
#The variables are the details of the car year make etc
#Parent super vehicle class using initializer method to be able to assign the attributes and then assign
#vehicleType attribute
class Vehicle:
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType

#Automobile class that inherits the attributes from Vehicle class with the additional required attributes
class Automobile(Vehicle):
    def __init__(self, vehicleType, year, make, model, doors, roof):
        super().__init__(vehicleType)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
#Define function to print the vehicle attributes
#This function will be called to print the vehicle information after it has been entered
#accessing the user imputs and assigning them to the attributes of Automobile class
    def displayInfo(self):
        print("Vehicle type:", self.vehicleType)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)

#Function to accept user input for a car
def getInfo():
    vehicleType = input("Enter vehicle type (car or truck): ")
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")
#create an new instance of Automobile class with the user input as attributes that will print the displayInfo function 
#from Automobile class
    car = Automobile(vehicleType, year, make, model, doors, roof)
    print("Vehicle Information:")
    car.displayInfo()

#call getInfo function to start program
getInfo()
