"""
0.initial setup:
a.create a variable and assign it a list of all integers
"""

var = [0, -9, 4, 21]

"""
1.printing a list's elements using a for loop in a function:
a.create a function that will take a list as its input and prints that list's elements using a for loop
b.call the function you created in step 1.a. with the list you created in step 0.a. as its input.
"""
def fun(list):
    for items in list:
        print(items)

fun(var)

"""
2.generating lists using range():
a.use range() to generate a list that starts at 0 and ends at and includes 9 (range should only have 1 input.)
Assign
 this range() to a variable
b.use range () to generate a list that starts at 4 and ends at and includes 7 (range should only have 2 inputs.)
Assign
 this range() to a variable
c.use range to generate a list that starts at 5, increments up in steps of 5, and ends at and includes 20 (range
should
 have 3 inputs.) Assign this range() to a variable.
"""
list1 = list(range(10))

list2 = list(range(4, 8))

list3 = list(range(5, 21, 5))

"""
3.passing a list made using a range into a function:
a.create a function that takes and returns 1 input
b.print a call of the function you created in step 3.a. with the range you made in step 2.a. as its input
"""
def simple(a):
    return a

print(simple(list1))
"""
4.iterating through a list using range() and a for loop:
a.create a function that uses a for loop and a range (as was shown in the lecture video) to print all of the
elements
 from a list.
b.call the function you created in step 4.a. with the range you made in step 2.b. as its input.
"""
def print_fun(li):
    for items in list(range(0, len(li))):
        print(li[items])

print_fun(list2)
"""
5.modifying elements from a list using range:
a.Create a function that uses a for loop and a range() to iterate through and add 3 to each of the elements
from a list.
 The function should print the modified list.
b.call the function you created in step 5.a. with the list you made in step 0.a. as its input.
"""
def add_fun(li):
    for items in list(range(0, len(li))):
        li[items] += 3
        print(li)

add_fun(var)


"""
6.passing multiple lists into a function:
a.Create a function that takes and prints 2 inputs.
b.Call the function you created in step 6.a. with the list you modified in step 5.b. and the range() you made in
step
 2.c.
"""
def two_inputs(x, y):
    print(x, y)

two_inputs(var, list3)
"""
7.Iterating through a list of lists using a function:
a.Create a list that contains 3 lists. Each of those lists should be composed of all strings.
b.Create a function that appends all of the strings from the list you made in step a into a new, single list.
(This
 function should use 2 for loops.) This function should print the new list.
c.Call the function you made in step 7.b. using the list you created in step 7.a. as its input.
"""
three_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def single_list(li):
    onelist = []
    for items in li:
        for nums in items:
            onelist.append(nums)
    print(onelist)

single_list(three_lists)

