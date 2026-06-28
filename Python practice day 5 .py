# format specifiers = basically helps to format strings better

cost1 = 874536468
cost2 = 3456.78332232
cost3 = 12

print(f"cost 1 {cost1: 3,}")
print(f"cost 2 {cost2: >123.2f}")
print(f"cost 3 {cost3: 34}")


cost23 = -3444.5334333
cost24 = 2233323.443999
cost25 = 90.356

print(f"cost 23 is {cost23:+,.2f}")
print(f"cost 24 is {cost24:>+12,.3f}") #alignment,+, width, round-off


#while loop = keeps repeating the condition until the condition is satisfied

ask = int(input("Your age: "))

while ask <1 or ask > 10 :
    print("Your age is invalid!")
    ask = int(input("Your age: "))

print(f"Your age is {ask} and valid for chocolates")


ask2 = input("What's your fav food?(Press 'S' to stop): ")

while not ask2 == 'S':
    print(f"You like {ask2}")
    ask2 = input("What's your fav food?(Press 'S' to stop)")

print("You have exited!")


#Write a script that tracks a bank account balance as it grows over time. The loop should run until the balance doubles, and print the formatted balance for each yea

balance = 1000
target = balance*2
intrest_rate = 0.05
year = 1

while balance < target :    #while - read it as when
    balance = balance + (balance*intrest_rate)
    print(f"Year{year} your balance is ${balance:<+12,.2f}")
    year = year+1

print(f"Here's the final money ${balance:<+,.2f}")

#This was awseome exercise!




    
    




