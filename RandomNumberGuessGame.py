import time
import random
attemps_count = 1
user_input=0
print("Welcome! Do you feel lucky today? Let's check it then :D")
print("Enter a range that you want to pick a number from!")
range_min = int(input("min: "))
range_max = int(input("max: "))
random_number = random.randint(range_min, range_max)
range_difference = range_max - range_min
points = 100
while user_input != random_number:
    user_input = int(input("Predict the number: "))

    if user_input > random_number:
        print("Nope, go down :)")
        attemps_count += 1
        
        
    elif user_input < random_number:
        print("Nope, go up :)")
        attemps_count += 1
        
        
    else:
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        print("You did it!!!")
        points = ((range_difference - (attemps_count * (range_difference*0.1) ) +1) / range_difference) * 100
        points = int(points)
        print (f"Score: {points}%")
        continue
