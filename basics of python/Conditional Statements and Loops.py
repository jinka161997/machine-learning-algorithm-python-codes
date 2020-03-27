# If
# If the number is positive, we print an appropriate message

num = -2
if num > 0:
    print(num, "is a positive number.")
    
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")


# If else:
num = 8

if (num >= 0):
    print("Positive or Zero")
else:
    print("Negative number")



## Define a function with conditional statement

def max_num(num1,num2,num3):

    if num1 >= num2 and num1 >= num3:

        return num1

    elif num2 >= num1 and num2 >= num3:
        return num2

    else:
        return num3

print (max_num(400,60,1150))

# Nested If
num = int(input("Enter a number: "))


if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

############# Loops #####################
# for Loop
# for each item in sequence , last item reached , no - body of loop , yes , exit loop


#Ex:1

snacks = ['pizza','burger','shawarma','franky']

for x in snacks:
    print("current snack: ", x)

print("Good day!")




#Ex:2

num = int(input("number: "))
factorial =1

if num < 0:
    print("must be positive")
elif num == 0:
    print("factorial = 1")
else:
    for i in range(1,num+1):
        factorial = factorial * i
    print("factorial =  " ,factorial)




#Nested for loop

for i in range(0,3):
    for j in range(0,3):
        print(i,j)

# For loop with else:
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")


########################## While Loop #############################
# Program to add natural
# Enter the loop , test expression , true , body of code , if false - exit loop.
# numbers upto
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)


# While loop with else
# Example to illustrate
# the use of else statement
# with the while loop

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")



#Ex: 1

count = 0

while count < 20:
    print("Digit: ", count)
    count = count + 1

print("Thank you")

#Ex: 2

import random

n = 20

random_number = int(n * random.random())

guess = 0

while guess != random_number:
    guess = int(input("New Number: "))
    if guess > 0:
        if guess > random_number:
            print("number is too large")
        elif guess < random_number:
            print("number is too small")
    else:
        print("sorry that you are giveup!")
        break
else:
    print("Congratulations. YOU WON!")


################### Modules#################################
#Ex:1

import math

x = 16
math.sqrt(x)

math.pow(2,5)


#Ex:2

import calendar

cal = calendar.month(2019,10)

print(cal)

calendar.isleap(2018)

calendar.isleap(2020)

dir(calendar)




