"""
Single parameter and zero parameter functions:
1.define a function that takes no parameters and prints a string
2.create a variable and assign it the value 5
3.create a function that takes a single parameter and prints it
4.call the function you created in step 1
5.call the function you created in step 3 with the variable you made in step 2 as its input
"""
# ----------------------------------------------------------------------------------------------------------------------
# Exercise 1

def f():
    print("Ciao!")


# Exercise 2

var = 5

# Exercise 3

def single(a):
    print(a)

# Exercise 4

f()

# Exercise 5

single(var)

# ----------------------------------------------------------------------------------------------------------------------
"""
multiple parameter functions:
1.create 3 variables and assign integer values to them
2.define a function that prints the difference of 2 parameters
3.define a function that prints the product of the 3 variables
4.call the function you made in step 2 using 2 of the variables you made for step 1
5.call the function you made in step 3 using the 3 variables you created for step 1
"""
# ----------------------------------------------------------------------------------------------------------------------

# Exercise 1

a = 2
b = 3
c = 5

# Exercise 2

def diff(x, y):
    print(x-y)

# Exercise 3

def prod(a, b, c):
    print(a * b * c)

# Exercise 4

diff(a, b)

# Exercise 5

prod(a, b, c)
# ----------------------------------------------------------------------------------------------------------------------
"""
Calling previously defined functions within functions:
1.create 3 variables and assign float values to them
2.create a function that returns the quotient of 2 parameters
3.create a function that returns the quotient of what is returned by the function from the second step and a
third
 parameter
4.call the function you made in step 2 using 2 of the variables you created in step 1. Assign this to a
variable.
5.print the variable you made in step 4
6.print a call of the function you made in step 3 using the 3 variables you created in step 1
"""
# ----------------------------------------------------------------------------------------------------------------------

# Exercise 1

bim = 1.2
bum = 3.4
bam = -10.7

# Exercise 2

def quot(x, y):
    return x / y

# Exercise 3

def multiquot(f, g, z):
    output = quot(f, g) / z
    return output

# Exercise 4

result1 = quot(bim, bum)

# Exercise 5

print(result1)

# Exercise 6

print(multiquot(bim, bum, bam))
# ----------------------------------------------------------------------------------------------------------------------
