#lab14.py

# Starter code for lab 14 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Joana Ugarte
# joanau@uci.edu
# 44875730


from abc import ABC, abstractmethod
import random,enum

class _Dog_:
    self._gender = str
    self._age = int
    self.hunger_clock = int
    self.appetite = str

class Husky:
    def __init__(self, name, age, appetite:Appetite=Appetite.MEDIUM):
        self._name = name
        self._age = age 
        self.hunger_clock = 0
        self.appetite = appetite

    def breed(self):
        return "Husky"
    
    def name(self):
        return self._name
    
    def age(self):
        return self._age

    def hungry(self):
        """
        The hungry method will check the hungry clock to see if some time has
        passed since the last feeding. If clock is greater than breed typical
        appetite, hunger assessment is randomly selected, otherwise hunger clock increases
        """
        if self.hunger_clock > self.appetite:
            return bool(random.getrandbits(1))
        else:
            self.hunger_clock += 1
            return False

    def feed(self):
        """
        Feeds the dog. Hunger clock is reset
        """
        self.hunger_clock = 0

class Pitbull:
    def __init__(self, name, age, appetite:Appetite=Appetite.MEDIUM):
        self._name = name
        self._age = age 
        self.hunger_clock = 0
        self.appetite = appetite

    def breed(self):
        return "Pitbull"
    
    def name(self):
        return self._name
    
    def age(self):
        return self._age

    def hungry(self):
        """
        The hungry method will check the hungry clock to see if some time has
        passed since the last feeding. If clock is greater than breed typical
        appetite, hunger assessment is randomly selected, otherwise hunger clock increases
        """
        if self.hunger_clock > self.appetite:
            return bool(random.getrandbits(1))
        else:
            self.hunger_clock += 1
            return False

    def feed(self):
        """
        Feeds the dog. Hunger clock is reset
        """
        self.hunger_clock = 0

class GermanShepherd:
    def __init__(self, name, age, appetite:Appetite=Appetite.MEDIUM):
        self._name = name
        self._age = age 
        self.hunger_clock = 0
        self.appetite = appetite

    def breed(self):
        return "German Shepherd"
    
    def name(self):
        return self._name
    
    def age(self):
        return self._age

    def hungry(self):
        """
        The hungry method will check the hungry clock to see if some time has
        passed since the last feeding. If clock is greater than breed typical
        appetite, hunger assessment is randomly selected, otherwise hunger clock increases
        """
        if self.hunger_clock > self.appetite:
            return bool(random.getrandbits(1))
        else:
            self.hunger_clock += 1
            return False

    def feed(self):
        """
        Feeds the dog. Hunger clock is reset
        """
        self.hunger_clock = 0

if __name__ == '__main__':
    breed = input("Please enter dog breed.")
    name = input("Please enter dog name.")
    age = int(input("Please enter dog age."))
    dog = breed(name, age, Appetite.HIGH)

    q = False
    while q == False:
        h = ""
        if dog.hungry() == False:
            h = "not "
        print(f"Your {dog.breed()}, {dog.name()} is {h}hungry.")
        feed = input(f"Would you like to feed {dog.name()}? (y/n/q): ")

        if feed == "y":
            dog.feed()
        elif feed == "q":
            break
