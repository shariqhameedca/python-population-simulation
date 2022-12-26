import random

class Person:
    def __init__(self, age):
        self.gender = random.randint(0,1)
        self.age = age