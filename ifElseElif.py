"""
For this problem you are going to make a program that simulates the output of a vending machine that only takes in
coins of American currency.
1.Your program should take an integer as an input from the user (either a 1, 2, or 3) that corresponds with an option
 for a drink from the vending machine outlined below and assign the corresponding price to a variable as a float.
 Use your knowledge of if, elif, and else statements to complete this part of the problem. Your code should
 have an else statement that prints a message and ends the program using sys.exit() if the user does not enter a valid
 input number.
 Vending Machine:
 1.water = $1.00
 2.cola = $1.50
 3.gatorade = $2.00
2.After placing an order, the user should be prompted to enter inputs 4 times:
 1.The first time, the user should be prompted to enter the number of quarters they put in the machine. Assign this
 number to a variable as an integer.
 2.The second time, the user should be prompted to enter the number of dimes they put in the machine. Assign this
 number to a variable as an integer.
 3.The third time, the user should be prompted to enter the number of nickles they put in the machine. Assign this
 number to a variable as an integer.
 4.The fourth time, the user should be prompted to enter the number of pennies they put in the machine. Assign this
 number to a variable as an integer.
3.Create a variable to hold the total value of all the coins the user has put into the machine.
4.Use flow control statements to print the user's change or output a message asking the user to try again depending
 on whether the total value of the coins the user has put into the machine is enough to pay for the item they ordered.
New knowledge for this problem:
1.%f format specifier
2.import sys and sys.exit()
3.int()
"""
# Exercise 1

drink = input("Choose your drink")
if int(drink) == 1:
    price = 1.00
    print("Please add $ " + str(price))
elif int(drink) == 2:
    price = 1.50
    print("Please add $ " + str(price))
elif int(drink) == 3:
    price = 2.00
    print("Please add $ " + str(price))
else:
    import sys
    sys.exit("Wrong selection. Please enter a valid code for your drink")

# Exercise 2

input1 = input("How many quarters did you add?")
quarters = int(input1)

input2 = input("How may dimes did you add?")
dimes = int(input2)

input3 = input("How many nickles did you add?")
nickles = int(input3)

input4 = input("How many pennies did you add?")
pennies = int(input4)

# Exercise 3

total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

# Exercise 4
"""
--- My original code ---
if total > price:
    print("Please collect your item and take your change: $ " + str(total - price))
elif total == price:
    print("Please collect your item. No change due.")
else:
    print("Insufficient credit. Please try again")

-- Better solution is below ---
"""
if total >= price:
    print("Your change is $ " + "%.2f" % (total - price) + ". Have a nice day!")
else:
    print("Insufficient credit. Please try again")