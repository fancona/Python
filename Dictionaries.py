"""
Creating Dictionaries, Accessing by Key, Adding to Dictionaries, and Length of a Dictionary:
1.create a 3 key: value pair dictionary and assign it to a variable
2.access and print a value from the list in step 1 by key
3.add a fourth key: value pair to the dictionary from step 1
4.print the dictionary from step 3
5.print the length of the dictionary from step 3
"""
# ----------------------------------------------------------------------------------------------------------------------

#1
cities = {10 : "Bari", 20 : "Rome", 30 : "Milan"}

#2
print(cities[10])

#3
cities[40] = "Lecce"

#4
print(cities)

#5
print(len(cities))

# ----------------------------------------------------------------------------------------------------------------------
"""
Reassignment by Key and Del:
1.create a 2 key: value pair dictionary and assign it to a variable
2.print the dictionary from step 1
3.reassign a key from the dictionary in step 1 a different value than its original value
4.print the dictionary from step 3
5.remove a key: value pair from the dictionary from step 3 using del
6.print the new dictionary
"""
# ----------------------------------------------------------------------------------------------------------------------

#1
sisters = {5 : "Federica", 19 : "Valentina"}

#2
print(sisters)

#3
sisters[5] = "Beatrice"

#4
print(sisters)

#5
del sisters[19]

#6
print(sisters)

# ---------------------------------------------------------------------------------------------------------------------