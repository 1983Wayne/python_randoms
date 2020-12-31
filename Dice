import random

class Die:
    def __init__(self, sides):
        self.sides = sides
        self.value = 1
        
    def roll(self):
        self.value = random.randint(1, self.sides + 1)
        return self.get_value()
        
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
