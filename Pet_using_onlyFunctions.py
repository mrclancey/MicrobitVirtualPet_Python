from microbit import *
import random
import time

# Define initial properties of virtual pet
pet_name = "My Pet"
pet_health = 100
pet_happiness = 100
pet_hunger = 0

# Define functions for virtual pet
def feed():
    global pet_hunger
    global pet_health
    pet_hunger -= 10
    if pet_hunger < 0:
        pet_hunger = 0
    pet_health += 5
    if pet_health > 100:
        pet_health = 100

def play():
    global pet_happiness
    global pet_health
    pet_happiness += 10
    if pet_happiness > 100:
        pet_happiness = 100
    pet_health -= 5
    if pet_health < 0:
        pet_health = 0

def display_status():
    display.scroll("Name: " + pet_name + " Health: " + str(pet_health) + " Happiness: " + str(pet_happiness) + " Hunger: " + str(pet_hunger))

while True:
    if button_a.was_pressed():
        feed()
        display_status()
        time.sleep(1)
        
    if button_b.was_pressed():
        play()
        display_status()
        time.sleep(1)
