# initialize class car (brand,color,year,speed,orientation)
# in case args speed and orientation are null they get default values
class car:
    def __init__(self, brand, color, year, speed=0, orientation="straight"):
        self.brand = brand
        self.color = color
        self.year = year
        self.speed = speed
        self.orientation = orientation

    # function speed_up gets arg int
    def speed_up(self, speed):
        self.speed += speed
        return self.speed

    # function turn gets arg str
    def turn(self, orientation):
        self.orientation = orientation
        return self.orientation


convertible = car("BMW", "black", 2010)
print(convertible.brand, convertible.color, convertible.year, convertible.speed, convertible.orientation)
convertible.turn("right")
print(convertible.brand, convertible.color, convertible.year, convertible.speed, convertible.orientation)
sedan = car("Nissan", "red", year=2019)
print(sedan.brand, sedan.color, sedan.year, sedan.speed, sedan.orientation)
sedan.speed_up(speed=90)
print(sedan.brand, sedan.color, sedan.year, sedan.speed, sedan.orientation)
