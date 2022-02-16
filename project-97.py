import time
import random


print("loading...")
#time.sleep(3)

print("Hello")
#time.sleep(2)

print("Welcome to 'The Number Guessing Game'")
#time.sleep(1)

print("i have chosen a number from 1 - 9 and u have to guess it")
chosenNumber = random.randint(0,22)
x = int(input("guess your number -- "))
print(x)

while(x!=chosenNumber) : 
    if(x > chosenNumber):
        print("little lower")
    elif(x<chosenNumber) :
        print("little higher")

    x = int(input("guess the number again --"))

print("hooray")