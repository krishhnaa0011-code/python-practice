# A temp converter from C to F or vice-versa
temp = float(input("what's the thermometer reading?: "))
unit = input("what's the unit of temp? Celsius or Fhrenheit (c or f): ")

if unit == 'c' :
    temp = round((temp*9) /5 + 32 , 3)
    unit = 'F'
elif unit == 'f':
    temp = round((temp-32) * 5/9 , 3)
    unit = 'C'

print(f"Your temperature is {temp} degree {unit}")

#Logical operator- or, and, not
#or- multiple if == can be used and either one of em shd be true
#and- both the if shd be true 
#not-just inverts the cmd if true it becomes false and if false becomes true

temp1 = 33
is_sunny = False

if temp1 > 35 or temp1 <= 0 or  is_sunny : #we can add multiple if with 'or'
    print("The trip is cancelled due to bad weather!")
else:
    print("The trip is on!")

temp2 = 23
is_sunny2 = False
if temp2 > 50 and is_sunny2:
    print("pEOPLE WILL GET BOILED OUTSIDE")
elif temp2 < 10 and is_sunny2:
    print("RUSSIA'S WEATHER OUTSIDE GNG")
elif 35 > temp2 > 0 and is_sunny2 :
    print("A NORMAL DAY FOLKS")
elif temp2 < 35 and not is_sunny2:
    print("Could rain today folks")

#okay so 'not' can be a little tricky 
user_id = False
if not user_id :    #read it like this is it true tht this is not the user id then print this
    print("Permission denied!")
else:
    print("Permission Granted!")

fall = True
if not fall:   #is it true tht u didnt fall then print this
    print("Back to work!")
else: 
    print("Take some pills")


#Okay so u can also play with strings
#with len(name)- to get the length
# with name.find()- to find smth
# with name.capitalise()- to capitalise first the letter
# with name.upper()- to capitalise every alphabet
#with name.lower()- puts eveything to lower case
# with name.isdigit()- if there's any digit it says true
#with name.isalpha()- if there is any alphabet it says yes
# with name.count()- it counts the numbers
# with name.replace it just replaces
#etc... print(help(str)) to get em all whenever necessary

name = input("Give us ur full name")


#end of day 3





  

