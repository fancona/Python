"""
and, or, and not:
1.create a variable and set it equal to True using a statement containing an "and" Boolean operator
2.create a variable and set it equal to False using a statement containing an "and" Boolean operator
3.create a variable and set it equal to True using a statement containing an "or" Boolean operator
4.create a variable and set it equal to False using a statement containing an "or" Boolean operator
5.create a variable and set it equal to True using a statement containing an "not" Boolean operator
6.create a variable and set it equal to False using a statement containing an "not" Boolean operator
"""
# type your code for "and, or, and not" below this comment and above the one below it. ---------------------------------

ex1 = 5 == 5 and 4 > 3
print(ex1)

ex2 = 5 != 4 and 3 < 2
print(ex2)

ex3 = 10 > 4 or 3 == 2
print(ex3)

ex4 = 3 <=1 or 1.5 >=5
print(ex4)

ex5 = not 5 // 4 > 3
print(ex5)

ex6 = not 5 % 4 == 1
print(ex6)

# ----------------------------------------------------------------------------------------------------------------------
"""
order of operations for Boolean operators:
1.make var1 evaluate to False by changing or removing a single Boolean operator
2.make var2 evaluate to True by changing or removing a single Boolean operator
"""
# type your code for "order of operations for Boolean operators" below this comment and above the one below it. --------
var1 = not 3 > 1 and 5 != 2 and 6 == 6
print(var1)
"""
Before change:
var1 = ​not ​3 ​> ​1 ​and ​5 ​!= ​2 ​or ​6 ​== ​6
var1 = not true and true or true
var1 = false and true or true
var1 = false or true
var1 = true
"""
var2 = 4 * 2 != 6 or not 7 % 6 == 1
print(var2)
"""
Before change:
var2 = ​4 ​* ​2 ​!= ​6 ​and not ​7 ​% ​6 ​== ​1
var2 = true and not true
var2 = true and false
var2 = false
"""
# ----------------------------------------------------------------------------------------------------------------------