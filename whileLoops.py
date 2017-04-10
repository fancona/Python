"""
1.While Loop Basics
a.create a while loop that prints out a string 5 times (should not use a break statement)
b.create a while loop that appends 1, 2, and 3 to an empty string and prints that string
c.print the list you created in step 1.b.
"""
counter = 3
empty = []
while counter < 9:
    empty.append([1,2,3])
    counter += 1
print(empty)
"""
2.while/else and break statements
a.create a while loop that does the same thing as the the while loop you created in step 1.a. but uses a break
statement
 to end the loop instead of what was used in step 1.a.
b.use the input function to make the user of the program guess your favorite fruit
c.create a while/else loop that continues to prompt the user to guess what your favorite fruit is until they guess
 correctly (use the input function for this.) The else should be triggered when the user correctly guesses your
 favorite fruit. When the else is triggered, it should output a message saying that the user has correctly guessed
 your favorite fruit.
"""
counter = 3
empty = []
while True:
    empty.append([1, 2,3])
    counter +=1
    if counter > 8:
        break
print(empty)

answer = input("What is my favourite fruit?")
while answer != "peach":
    print("Wrong answer. Try again!")
    answer = input("What is my favourite fruit?")
else:
    print("That's right, " + answer + " is my favourite fruit!")