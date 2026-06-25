
#validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

name = input("Your username please?: ")
if len(name) > 12 :
    print("Your username can't be more than 12 characters")

elif " " in name :
    print("You can't have space in the username")

elif not name.isalpha() :       #name.alpha() - means it is true if all the string is in letter
    print("You can't have digits in the username")              #name.digit()- means it is true if all are digits in a string

else:
    print(f"Welcome!, {name} Ram, Ram ")

# indexing = accessing elements of a sequence using [] start:end:step ; start:end is the range ; :step is the number of steps after which the num is there.
credit_number = "123-456-789"
num = credit_number[1:3] #012345 is how the sequencing is
print(num)

num2 = credit_number[ : :-2] #skips to the 2nd in reverse haha
print(num2)

num3= credit_number[-3 : ] #
print(f"your credit number is XXX-XXX-{num3}")


# format specifiers = basically helps to format strings better
# .(number)f= rounds to decimal places #f = fixed lock
# :(number)= allocates that many places
#  :< = moves to the left 
# :> = moves to the right
# :^ = centre align
# :+ = use a plus to indicate positbe value
# := = left most position
# :  = insert space before positibve numbers
# :, = comma seperator


#end of day 4





