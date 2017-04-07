"""
For Loops and Tuples Problems:
Tuples:
1.create a 4 element tuple that consists of a float, an integer, a Boolean value, and a string. Assingn this tuple to a
variable
2.print the tuple from step 1
3.print the the second element from the tuple you made in step 1 
4.print the first element from the tuple you made in step 1
5.slice and print the first 3 elements of the tuple from step 1 
6.slice and print the last 3 elements of the tuple from step 1 
7.slice and print the middle 2 elements of the tuple from step 1
"""
# ----------------------------------------------------------------------------------------------------------------------
#1
tuple = (1.57, 4, False, "Federica")

#2
print(tuple)

#3
print(tuple[1])

#4
print(tuple[0])

#5
print(tuple[:3])

#6
print(tuple[1:])

#7
print(tuple[1:3])

#  ----------------------------------------------------------------------------------------------------------------------
"""
For Loops:
1.create a variable and assign it the tuple ("Bohr", "Leibniz", "Einstein")
2.create a variable and assign it an empty list
3.create a variable and assign it the list [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
4.use a for loop to go through and print each of the elements from the tuple in step 1 individually 
5.use a for loop and .append() to add the middle 6 elements to the empty list from step 2
6.print the new list
"""
# ----------------------------------------------------------------------------------------------------------------------
#1
var = ("Bohr", "Leibniz", "Einstein")

#2
empty = []

#3
list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#4
for items in var:
    print(items)

#5
for nums in list[2:8]:
    empty.append(nums)

#6
print(empty)

#  ----------------------------------------------------------------------------------------------------------------------