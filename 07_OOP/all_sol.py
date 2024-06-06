class Car:
    total_car = 0
    # self is the connection string to the class
    # context = self which is this , current own instance, refering to oneself class
    # __init__ is also constructor
    def __init__(self, brand, model):
        # before any var 2 underscore it is called private attributes
        # now any object of the class can't access it
        self.__brand = brand
        self.__model = model
        # to count the total number of car object created
        # self.total_car += 1
        # or simply any time a car class object is made this constructor is called so this has instances of the total number of object made
        Car.total_car += 1


    #providing a gettter method for brand attribute to make it private
    def get_brand(self):
        return self.__brand + " This is private "
    
    # every private method should provide getter functions
    @property # property makes sure that it cant override the attribute
    def get_model(self):
        return self.__model
    
    def car_details(self):
        return f"The car Model is :{self.__model} and Brand is :{self.__brand} "
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    # static method belongs to the class instead of the instance(object) of the class
    # this @staticmethod keyword is called decorators
    @staticmethod #no need of self keyword cause static method not call by object access directly call by class so no any context required
    def general_desc():
        return "Cars are means of transport"
    


class ElectricCar(Car):
    def __init__(self,batterySize,brand,model):
        super().__init__(brand,model)
        self.batterySize =batterySize

    def fuel_type(self):
        return "Electric"
    

Tesl_car = ElectricCar('85KWH','Tesla','Model S')
print(Tesl_car.car_details())
print("My Tesla car is : "+Tesl_car.fuel_type())

""" Toyota_car = Car("Toyota","Corolla") # until the __init__ is not made the param cant be pass to class
# print(Toyota_car.brand)
print(Toyota_car.get_brand())
# when accessing private attribute use get_
# print(Toyota_car.model) #this will not work
print(Toyota_car.get_model)
print(Toyota_car.car_details())

# print(Toyota_car.get_model()) get_model is set as property decorator so it need to be accessed as reference not function call

Tata_car = Car("Tata","Safari")
print(Tata_car.car_details())
print(Tata_car.get_model)
print(Tata_car.fuel_type())

print(Car.total_car)

# accessing the static method general_desc
print(Car.general_desc()) """

# now checking if tesl_car is instance of car class and electricar clas
""" print(isinstance(Tesl_car, Car))
print(isinstance(Tesl_car, ElectricCar)) """

# checking multiple inheritance

# pass keyword is a method to be implemented later
class Battery:
    def battery_info(self):
        return "this is battery"
    # pass

class Engine:
    def engine_info(self):
        return "this is enigne"
    # pass

class HydrogenCar(Battery,Engine,Car):
    pass

hydro_car = HydrogenCar("Tesla","Hydro H")

print(hydro_car.engine_info())
print(hydro_car.battery_info())

# hence proved mulitple inheritance is there in pythond