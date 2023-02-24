import time
import random
random_number = random.randint(0, 100)
user_input=0
print("Welcome! We have a number which is chosen between 0-100. Would you predict it?")
while user_input != random_number:
    user_input = int(input("Predict the number: "))

    if user_input > random_number:
        print("Nope, go down :)")
    elif user_input < random_number:
        print("Nope, go up :)")
    else:
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        print("PERFECT!!! YOU ARE SO SMART!!! ;) ")
        continue
