#collections =
#  Lists[]- ordered and changeable, can duplicate 
# (Use a list when order matters and you want total freedom to change everything)

#Set {} - unordered and immutable but add/remove 
# (Use a set when you want to make sure every single item is unique, or to instantly clean out duplicates.)

#Tuple ()- ordered and unchangeable can duplicate and is faster
#Use a tuple when data must never change (like a password, username, or map coordinates). 
# Because it is locked, it has no functions to add or remove things

#Lists []
inventory = ["phone", "tab", "cable", "charger"]
#impt func's
inventory.append("shoes") #adds a data to the end
print(inventory)
inventory.insert(3, "keys") # to insert at a particular position
print(inventory)
inventory.remove("tab") #removes data
print(inventory)
inventory.sort()
print(inventory)
last_item = inventory.pop()
print(last_item)

#Sets {}
basket = {"apple", "banana", "orange", "apple"}
basket.add("carrot")      
print(basket) 
#basket.sort() this can;t bc u remember its an ordered list it's meant to be random
basket2 = {"jam", "biscoff", "bread"}
combined = basket.union(basket2)
print(combined)


#Tuples ()
coordinate=(2332.3, 2232.2)

pos = coordinate.index(2332.3)
print(pos)
count = coordinate.count(2232.2)
print(count)