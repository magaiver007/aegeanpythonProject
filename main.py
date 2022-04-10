class car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def speed_up(self, amount):
        self.speed_up += amount
        return self.speed_up

    def turn(self, orientation):
        self.turn += orientation
        return self.turn
