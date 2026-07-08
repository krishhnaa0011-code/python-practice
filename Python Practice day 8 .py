# creating a rectangle
ask = int(input("how many rows: "))
ask1 = int(input("how many coloumns: "))
ask3 = input("Enter any symbol: ")

for x in range(ask):
    for y in range(0,ask1):
        print(ask3,end=" ")
    print()


#a stop watch
import time
ask67 = int(input("Your time in seconds: "))

for z in reversed(range(0,ask67)):
    sec = int(z % 60)
    min = int((z / 60) % 60)
    hour = int(z / 3600)
    print(f"{hour:02}:{min:02}:{sec:02}")
    time.sleep(1)

print("time is up!")


#Odd or even
og_number = float(input("Give me a number: "))

ask99 = int(og_number % 2) 
ask98 = int(og_number % 4)

if ask98 == 0:
    print("Your number is even and your number divisible by 4 as well")
elif ask99 == 0:
    print("Your number is just even")


else:
    print("Your number is odd")


#collections = 

