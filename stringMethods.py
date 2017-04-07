"""
len() and str() practice:
1.create a variable and assign it the string "Python"
2.create another variable and assign it the length of the string assigned to the variable in step 1
3.create a variable and use string slicing and len() to assign it the length of the slice "yth" from the string assigned
 to the variable from step 1
4.create a variable and assign it the float 1.32
5.create a variable and assign it the string "2" from the float assigned to the variable from the last problem (use the
 str() string method for this)
"""
# type your code for "len() and str() practice" below this single line comment and above the one below it --------------

string = "Python"
length = len(string)
lenslice = len(string[1:4])
float = 1.32
convfloat = str(float)[3]
print(length)
print(convfloat)
# ----------------------------------------------------------------------------------------------------------------------
"""
.upper() and .lower() practice:
1.create a variable and assign it the string "upper" changed to "UPPER" using .upper()
2.create a variable and assign it the string "owe" from "LOWER" using string slicing and .lower()
"""
# type your code for ".upper() and .lower() practice" below this single line comment and above the one below it --------

varupper = "upper".upper()
print(varupper)

varlower = "LOWER"[1:4].lower()
print(varlower)

# ----------------------------------------------------------------------------------------------------------------------