"""
string and escape sequences:
1.create a variable and assign a string that is surrounded in double quotes to it
2.create a variable and assign a string that is surrounded in single quotes to it
3.create a variable and assign it a string that uses the double quote escape sequence within it
4.create a variable and assign it a string that uses the single quote escape sequence within it
"""
# type your code for "string and escape sequences" in between this single line comment and the one below it------------

str1 = "The capital of Italy is Rome"
str2 = 'The capital of the United Kingdom is London'
str3 = "Dante Alighieri wrote \"The Divine Comedy\""
str4 = 'William Shakespeare wrote \'Richard III\''

# ----------------------------------------------------------------------------------------------------------------------
"""
accessing values by index and string slicing:
1.create a variable called lannisters and assign it the string "JaimeCerseiTyrion"
2.create a variable and assign it the "a" from the string assigned to the variable lannisters.
3.create a variable and assign it the "J" from the string assigned to the variable lannisters.
4.create a variable and assign it "Jaime" from the string assigned to the variable lannisters.
5.create a variable and assign it "Cersei" from the string assigned to the variable lannisters.
6.create a variable and assign it "Tyrion" from the string assigned to the variable Lannisters.
"""
# type your code for "accessing values by index and string slicing" in between this comment and the one below it-------

lannisters = "JaimeCerseiTyrion"
ex1 = lannisters[1]
ex2 = lannisters[0]
ex3 = lannisters[:5]
ex4 = lannisters[5:11]
ex5 = lannisters[11:]

# ----------------------------------------------------------------------------------------------------------------------

print(str1, str2, str3, str4)
print (ex1, ex2, ex3, ex4, ex5)