"""
0.Setup:
a.create a list of integers and assign it to a variable
b.create a list of strings and assign it to a variable
c.create a list of floats and assign it to a variable
"""
integers = [1, -9, 4, 10]
strings = ["Batman", "Spiderman", "Superman"]
floats = [2.98, -87.3, 1.23]

"""
1.Passing A List to A Function:
a.create a function that takes and returns an input
b.print a call of the function you created in step 1.a. with the list of integers from step 0.a. as the input
c.print a call of the function you created in step 1.a. with the list of strings from step 0.b. as the input
d.print a call of the function you created in step 1.a. with the list of floats from step 0.c. as the input
"""
def fun(x):
    return x

print(fun(integers))
print(fun(strings))
print(fun(floats))

"""
2.Accessing An Element In A list using A Function:
a.create a function that takes a list as an input and returns one of that lists elements
b.print a call of the function you created in step 2.a. with the list of integers from step 0.a. as the input
c.print a call of the function you created in step 2.a. with the list of strings from step 0.b. as the input
d.print a call of the function you created in step 2.a. with the list of floats from step 0.c. as the input
"""
def funlist(li):
    return li[2]

print(funlist(integers))
print(funlist(strings))
print(funlist(floats))

"""
3.Modifying A List Element Within A Function:
a.create and call a function that prints the product of all the integers from the list you created in step 0.a.
b.create and call a function that concatenates all the strings from the list you create in step 0.b and prints the
 result
c.create and call a function that prints the quotient of all the floats from the list you created in step 0.c.
"""
"""
def prod(li):
    print(li[0*1*2*3])
prod(integers)"
"""
def prod(li):
    import operator
    import functools
    print(functools.reduce(lambda x,y: x*y, li, 1)) # 1 is initializer used when iteratable li is empty
prod(integers)

"""
can also use:
def prod(li):
    import operator
    import functools
    print(functools.reduce(operator.mul, li, 1))
prod(integers)

"""

"""
def conc(li):
    print(li[0] + li[1] + li[2])
conc(strings)
"""
def conc(li):
    holder = ""
    for x in li:
        holder += x
        print(holder)
conc(strings)

def div(li):
    import operator
    import functools
    print(functools.reduce(lambda x,y: x / y, li))
div(floats)

"""
4.Manipulating Lists Within Functions:
a.create a list that uses 3 of the following functions on one of the lists you created in part 0 of this problem set:
 .index(), .append(), .remove(), .insert, or .pop(). Also, make sure that the function prints the resulting list
b.call the function from part 4.a. using one of the lists you made in part 0 of this problem set.
"""
"""
multiple parameters example:

def newfun(li, x, y):
    li.pop(2)
    li.append(x)
    li.insert(0, y)
    print(li)

newfun(strings, "Thor", "Captain America")
"""

def newfun(li):
    li.append(li[0])
    li.remove(li[2])
    li.pop(2)
    print(li)

newfun(strings)
