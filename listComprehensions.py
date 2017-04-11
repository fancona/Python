"""
1.Basic List Comprehensions
a.use a basic list comprehension to generate and print the list [8, 6, 4, 2, 0]
b.use a basic list comprehension to generate and print the list [1, 4, 27, 256]
c.use a basic list comprehension to generate and print the list [24, 35, 48]
"""

# list1a = print([num - 2 for num in list(reversed(range(2, 11))) if num % 2 == 0])

#list1a without if statement

list1a = print([num for num in list(range(8, -2, -2))])

list1b = print([num ** num for num in list(range(1,5))])

list2c = print([num * (num - 2) for num in list(range(6, 9))])

"""
2.List Comprehensions with If Statements
a.use a list comprehension with an if statement to generate and print the list [2, 3, 4, 7, 8, 9]
b.use a list comprehension with an if statement to generate and print the list [10, 9, 8, 3, 2, 1]
c.use a list comprehension with an if statement to generate and print the list [1, 4, 5, 6, 9, 10]
"""
list2a = print([num for num in list(range(2, 10)) if num <= 4 or num >= 7])

list2b = print([num for num in list(reversed(range(1, 11))) if num > 7 or num < 4])

list2c = print([num for num in list(range(1, 11)) if num != 2 and num != 3 and num != 7 and num != 8])