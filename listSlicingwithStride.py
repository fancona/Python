"""
0.Setup
a.create a list of 13 integers and assign it to a variable
"""
int = [0, -2, 7, 1.4, 90, 76, 0.45, -8, -5.7, 129, 7, 4.3, 1]

"""
1.List Slicing With Stride
a.create a variable and assign it a list slice comprised of every 4th number from the list you made in step 0.a.
b.print the list slice from step 1.a.
"""

var1a = int[3:13:4]
print(var1a)

"""
2.List Slicing with Stride and Omitted start and end indices
a.using only stride, assign a list slice composed of every 3rd value from the list you made in step 0.a. to a
variable.
b.print the list slice from step 2.a.
"""

var2a = var1a[::3]
print(var2a)

"""
3.Reversing Lists with Stride
a.reverse the list you made in step 0.a. and assign it to a variable
b.print the reversed list you made in step 3.a.
"""
var3a = var1a[::-1]
print(var3a)