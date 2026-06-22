#Exercise 2 Shopping Cart with items, price and quantity

print("Welcome to Junkdog's shopping cart")
name = input("Hello pls give us ur name")
print(f"Hola! {name} looks like something is cooking!")

item = input("what are item would u like to buy:")
quantity = float(input("How many woud u like to buy: "))
price = float(input("At what price?: "))
grand_total = price*quantity + 35
print(f"So {name}, you you have selected {item} x {quantity}/s at ${price}, your grand total is ${grand_total} with a 35$ delivery charge")

#Exercise 3 madlibs game- story building with random words

name100 = input("Your name cutie: ")
print(f"Welcome to Madlib Games!, {name100}")

day_of_week = input("What day of the week is it? ")
adjective = input("enter an adejective an emotion: ")
location = input("Enter a location 'noun': ")
person_name = input("enter a person's name: ")
person_name2 = input("Enter another person's name: ")

print(f"I wrote my test {day_of_week} and it was was {adjective} but when I got {location} I was releived seeing {person_name} I accidently farted on {person_name2}, and then i woke up it was time to go to work")  
print("Lmao!")

#Math Arth operations- +,-,* is basic. ** is for to the power. % sign is to find the remained left after dividing
car = 100
car = car + 12
# or just do car += 12
car *= 24 #multi
car **= 3 #to the power
car /= 5  #divide
car %= 3  #remainder

print(car)

# round() for round off, ab() for modulus, pow() for to the power, max() for maximum value or min() for min value among the variables

X = 3.22223443
Y = 4.58938812
Z = 99.4987676
F = -35

answer = round(Y)
print(answer) # no need of "" thats only when string of text is to be sued

answer2 = pow(Z, 4)
print(answer2)

answer3 = abs(F)
print(answer3)

answer4 = min(X, Y, Z, F)
print(answer4)

answer5 = max(X, Y, Z, F)
print(answer5)

import math # it is math modules to utilise some of maths functions

print (math.pi)
G = 56
print(math.sqrt(G)) #its square root
H = 33.67
print(math.ceil(H)) #to round-off upwards

#Exercise - to calculate the circumference of the circle
import math

radius = float(input("yo give me the radius of ur circle: "))
circum = 2*math.pi*radius
circum2 = round(circum, 3)

print(f"your circumference is {circum2}cm")

#Exercise - to calculate the hypotenuse of the right-angled triangle

import math 
base = float(input("What is the length of the base: "))
perpend = float(input("What is the length of the perpendicular: "))

hypotenuse = math.sqrt(pow(base, 2) + pow(perpend, 2))
hypotenuse = round(hypotenuse, 3)

print(f"your hypotenuse is {hypotenuse}cm")

#If - do the print only if its true, ellif is used when if i hv to run smtg else, else is used as alternative and final resort similar to ellif only.

age99 = int(input("what's your age?"))
if age99 >= 18 :
   print ("Congrats! u are legal!")

elif age99 >= 100 :
   print ("Living Fossil!")

elif age99 <=0 :
   print ("Are you even born yet bro!")

else:
   print("Underage kiddo!")
#maybe this can be used for loans or porn websites stuff!


#We can use if and else with a boolean too 

user_online = False #Could b true as well

if user_online :
   print("Bring em online!")
else:
   print("he's already in!")

high = input("Are u high ' YES ' / ' NO ' ")
if high == 'YES' :
   print("Don't drive")
elif high == 'NO':
   print("You are safe to go")
else:
   print("answer the goddamn Q")


#Lets a calculator

select = input("Please select your math function u want to perform + - / * ")
num1 = float(input("Enter ur 1st number"))
num2 = float(input("Enter ur 2nd number"))

if select == '+' :
   ans = num1 + num2 
   print(ans)

elif select == '-' :
   ans = num1 - num2
   print(ans)
   
elif select == '/' :
   ans = num1 / num2
   print(ans)

elif select == '*' :
   ans = num1 * num2
   print(ans)
else :
   print("pls select the right one bruh!")

#AN kg to pound converter

weight = float(input("Tell us ur weight: "))
ask67 = (input("Type 'kg' for Kilogram or 'L' for Pound: "))

if ask67 == 'kg' :
   weight *= 2.205
   unit = "pound/s"
elif ask67 == 'L' :
   weight /= 2.205
   unit = "kg/s"
print(f"your weight is {weight} {unit}")  
    










