print("Hello MOM")
#This is my 1st python program

#Variables- it could strings, integer, f;oat, boolean.

#string 
name = "krishna"
print(f" Hello user your name is {name}")
food = "paneer"
print (f"Your fav food is {food}")
#f helps in formating what u write inside make sure to use {} for variable

#Integer- as u know its a whole no. and dont put this under "" because it becomes a text 
age = 19
dob = 2006
num_of_yr_of_edu = 12
print (f"Hello {name} your fav food is {food} your age is is {age} and you were born in {dob} with {num_of_yr_of_edu} years of education")
#whenever u write more than word on the left write like this new_word this tells python they are 2 diff words they are called snake case

#Floats- is for decimal numbers
price = 99.99
discount = 23.45
print (f"Hellow {name} your fav food {food} costs ${price} and it comes with a discount of ${discount}")
distance = 12.500
print(f"the distance between ur home and school is {distance}km")
#so you can aslo add km or $ but outside the {} as required front or back

#BOOlean-this one's nice it either is True or False with cap T or F and u can with this with else and if statement 
day_of_test = True
if day_of_test:
    print( "good luck champ do well!")
else:
    print("keep going it's closer than u think")
#read ':' as describe it'll be easy to remember

hurt = False
if hurt:
    print("take some rest")
else:
    print("keep grinding")

#Typecasting= this changes from one variable to another using str(), bool(), int(), float() 
integer = 102

integer = float(integer)
print(integer)

float = 123.45
float = int(float)
print(float)

naam = "siya ram"

naam = bool(naam)
print(naam)

naam2 = ""
naam2 = bool(naam2)
print(naam2)
# integer to float is easy, string to boolean is used to checck if the user has enterred their name or not

#input()  it takes info from the user in string only to form any other arithmatic func u need to typecaste it using int() or float()
name = input("your name  bbg?")
age = input("your age bbg?")
print(f"Hello {name} your age is {age}")
age = int(age) # had to do this bc input is only in string

age = age + 1
print(f"next yr u will be {age} years old")

#or just use int(input()) to avoid writing 2 lines for input and typecasting
age2 = int(input("your age bbg?"))
age2 = age2 +3
print(f"u shall be {age2} yrs in 3 yrs from now")

#exercise-1 we need to ask user length and width of rectangle and calculate area for it

length = int(input("describe the length of ur rectangle")) #ive converted string into int to perform arth operation
width =int(input("describe the width of it"))
if length > 0:
  print("got it")
else:
  print("pls input a valid response")

if width > 0:
  print("got it")
else:
  print("pls input a valid response")

area = length*width
print(f"your area is {area}sq units")

#End of day 1