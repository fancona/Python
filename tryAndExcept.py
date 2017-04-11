"""
1.Try and Except to handle divide by zero and type errors
a.Use input() to have the user enter two integers as inputs. Assign these to 2 different variables.
b.Define a function that takes two inputs. This function should print the result of the first input divided by the
 second input. Use your knowledge of Try and Except statements to print messages for the errors that would occur if
the
 second input of the function is 0 or if one or both of the inputs cannot be converted to integers.
c.call the function from step 1.b. with the 2 variables from step 1.a. as inputs.
"""

var1 = input("Enter your first integer")
var2 = input("Enter your second integer")

def fun(var1, var2):
    try:
        try:
            print(int(var1)/int(var2))
        except ZeroDivisionError:
            print("You cannot divide a number by 0")
    except:
        print("Both your first and second input need to be integers.")








fun(var1, var2)






