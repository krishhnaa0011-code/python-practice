import time

ask = int(input("Enter time in seconds:"))

for x in reversed(range(0, ask)):
    sec = int(x % 60) #lets say  we say ask = 180s then sec divides it by 60 % says abt remainder and here the remainder is 0 so sec:0

    minutes = int(x / 60) % 60 #then min 180/60 = 3 ; 3 % 60 is a very small remainder so it'll just display 3 in minutes

    hours = int(x / 3600)# similarly 180/3600 is less than 0 its not shown as 0 for the biggest variable we dont use % because it can infi>ask>1
    print(f" {hours:02}.{minutes:02}.{sec:02}")
    time.sleep(1)#the data blinks after each 1 sec

print("Time is up")


#nested loop = a loop within another loop. Outer loop is to print inner that many times
#inner loop like a normal loop does that like for would give range while would ask infi times repeat


for y in range(3): #outer loop
    for z in range(1,5):#inner loop
        print(z, end="")#basically at the end of each
    print()#adds space after every loop

#we can create a square or a rectangele w symbols or digi

ask1 = int(input("The no. of rows: "))
ask2 = int(input("The no. of coloumns: "))
ask3 = input("Enter a symbol: ")

for a in range(ask1):   #does rows
    for b in range(ask2):  #does coloums
        print(ask3, end=" ") #space at the end of each
    print()  #for space after each loop