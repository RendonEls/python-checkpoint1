# #1: Define a Vehicle class with the following properties and methods: 
# - `vehicle_type` 
# - `wheel_count`
# - `name` 
# - `cost` 
# - `colors` 
# - `vehicle_brand` 
# - `mpg`, a 'dict', with the following properties:
#     - `city`
#     - `highway` 
#     - `combined` 
# - `get_vehicle_type` should return the `vehicle_type`
# - `get_vehicle_brand` should return the classes `vehicle_brand`
# - `get_vehicle_drive` if the `wheel_count` for that class is "no wheels!" then
#     it should return "no wheels send it back to the shop" otherwise it should
#     return "I have "  + self.wheel_count  + " wheel drive"
#
# Your Vehicle class should take one argument (a `dict`) with the above
# attributes. Define the properties on the class from the dict that is passed in.

class Vehicle: 
    def __init__(self, vehicle_type, wheel_count, name, cost, colors, vehicle_brand):
        self.vehicle_type = vehicle_type
        self.wheel_count = wheel_count
        self.name = name
        self.cost = cost
        self.colors = colors
        self.vehicle_brand = vehicle_brand
        self.mpg = {
            "city": '',
            "highway": '',
            "combined": ''
        }

    def get_vehicle_type(self):
        print(self.vehicle_type)
    def get_vehicle_brand(self):
        print(self.vehicle_brand)
    def get_vehicle_drive(self):
        if self.wheel_count == "no wheels!":
            print("no wheels send it back to the shop")
        else: 
            print(f"i have {self.wheel_count} wheel drive")


# #2: Create a Motorcycle class that inherits from the Vehicle class and has the
# following properties and methods:
# - property: `wheel_count` defaults to "no wheels!"
# - method: `pop_wheelie` if `wheel_count` is not equal to 2 then it should be False,
#       otherwise return "......pop!"

class Motorcycle(Vehicle):
    pass


# #3: Define a Car class that inherits from the vehicle class with the following attributes and methods:
# - property: `wheel_count` defaults to 4
# - method: `can_drive` that should return 'Vrrooooom Vroooom'

class Car(Vehicle):
    def __init__(self):
        pass


# #4: Define a Truck class that inherits from the vehicle class with the following attributes and methods:
# - property: `wheel_count` defaults to "no wheels!"
# - method: `rev_engine` that should return 'revvvvvreeeev'

class Truck(Vehicle):
    def __init__(self, wheel_count):
        pass

# Commit when you finish working on these questions!