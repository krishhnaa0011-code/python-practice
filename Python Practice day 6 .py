#Python Compound Intrest Calculator
ask1 = float(input("Enter your principle amt.: "))
             
while ask1 < 0 :
    print("Your principle can't be that")
    ask1 = float(input("Enter your principle amt.: "))

ask2 = float(input("Enter your intrest rate: "))
while ask2 < 0 :
    print("Your intrest rate can't be that")
    ask2 = float(input("Enter your intrest rate: "))

ask3 =float(input("Enter your time in years: "))
while ask3 < 0 :
    print("Your time period can't be that")
    ask3 =float(input("Enter your time in years"))

sum = ask1 * pow((1+ask2/100) , ask3)
print(f"Your final amt. will be ${sum:<+12,.3f} in {ask3} year/s")

#For loop- helps in putting out a range for strings, int etc..

for x in range(1,21): 
    if x == 13 or x == 8 :
        continue
    else:
        print(x)


for c in reversed(range(1, 20)):
    print(c)
print("Happy B-day")

for d in range(1,20, 2): 
    print(d)


#End of day 6


        

                  


