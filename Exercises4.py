#1
'''
x = 0
while x < 1000:
    if x % 3 == 0:
        print(x)
    x += 1



#2

user_num = float(input("Enter a number you want to convert, or enter a neg value to stop: "))
while user_num >= 0:
    user_num_cn = user_num * 2.54
    print(user_num_cn)
    user_num = float(input("Enter a number you want to convert, or enter a neg value to stop: "))



#3

user_num = input("Enter a number, or enter an empty string to stop: ")
smallest_num = 0.0
biggest_num = 0.0
while user_num != "":
    user_num = float(user_num)
    smallest_num = user_num
    if user_num < smallest_num:
        smallest_num = user_num
    if user_num > biggest_num:
        biggest_num = user_num
    user_num = input("Enter a number, or enter an empty string to stop: ")
print(f"Smallest number: {smallest_num} Biggest number: {biggest_num}")


#4

from random import randint

x = randint(1, 10)
user_guess = int(input("Enter a number to guess: "))

while user_guess != x:
    if user_guess < x:
        print("Too low")
    elif user_guess > x:
        print("Too high")
    user_guess = int(input("Enter a number to guess: "))

print("Correct!")




#5

true_username = "python"
true_password = "rules"

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    if username == true_username and password == true_password:
        print("Welcome")
        break
    else:
        print("Wrong password and/or username, try again")
        attempts += 1

if attempts == max_attempts:
    print("Access denied")

'''

#6

import random

number = int(input("Insert a large number of points: "))
squarePoints = list(range(2))
circlePoints = int()

for i in range(0, number):
    squarePoints = [random.uniform(-1, 1), random.uniform(-1, 1)]

    if (squarePoints[0] ** 2 + squarePoints[1] ** 2) < 1:
        circlePoints += 1

print("The approximate value of pi is:", 4 * circlePoints / number)