# NIKOS BOUSIS 2022
# in case args speed and orientation are null they get default values
# initialize class car (brand,color,year,speed,orientation)
class car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
        self.speed = int()
        self.orientation = ""

    # function turn gets arg str
    def turn(self, orientation):
        self.orientation = orientation
        return self.orientation

    # function speed_up gets arg int
    def speed_up(self, speed):
        self.speed += speed
        return self.speed


convertible = car("BMW", "μαύρο", 2010)
print(convertible.brand, convertible.color, convertible.year, convertible.orientation)

convertible.turn("δεξιά")
print(convertible.brand, convertible.color, convertible.year, convertible.orientation)

sedan = car("Nissan", "κόκκινο", year=2019)
print(sedan.brand, sedan.color, sedan.year, sedan.speed, sedan.orientation)

sedan.speed_up(speed=90)
print(sedan.brand, sedan.color, sedan.year, sedan.speed, sedan.orientation)
