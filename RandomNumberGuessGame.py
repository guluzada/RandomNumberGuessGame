import time
import random
a = random.randint(0, 100)
b=0
print("Welcome! We have a number which is chosen between 0-100. Would you predict it?")
while b != a:
    b = int(input("Predict the number: "))

    if b > a:
        print("Nope, go down :)")
    elif b < a:
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
