name1 = input("What is your Name AGENT?")
print("Hello, " + name1 + " Do you require a secret mission?")
name2 = input("Yes or No?")
if name2.lower() == "yes":
    print("Excellent! Your mission, should you choose to accept it, is to infiltrate the enemy base and retrieve the secret documents.")
elif name2.lower() == "no":
    print("Understood. Stay safe, Agent " + name1 + ".")
