'''
#1

from random import randint

def dice_roll ():
    rolled_num = randint(1,6)
    return rolled_num

rolled_num = 0

while rolled_num != 6:
    rolled_num = dice_roll()
    print(rolled_num)



#2

from random import randint

num_of_sides = int(input("How many sides do you want?"))

def dice_roll (sides):
    rolled_num = randint(1,sides)
    return rolled_num

rolled_num = 0

while rolled_num != num_of_sides:
    rolled_num = dice_roll(num_of_sides)
    print(rolled_num)




#3

gallons = 0
def gall_to_l(amount):
    l = amount * 3.785
    return l
while gallons >= 0:
    gall=float(input("Enter the volume in american gallons to convert it to,"))
    if gallons < 0:
        break
    converted = gall_to_l(gallons)
    print("The number in liters = ", converted)



#4

def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


test_list = [1, 2, 3, 4, 5]
result = sum_of_list(test_list)
print(f"The sum of the list {test_list} is: {result}")



#5

def remove_odd_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = remove_odd_numbers(original_list)

print("Original list:", original_list)
print("Even numbers list:", even_list)


'''

#6

import math

def pizza_per_m2(diameter, price):
    area = math.pi*(diameter/2)**2
    pizza_per_m2 = price/area
    return pizza_per_m2

diam_1 = float(input("Enter the diameter of the first pizza: "))
diam_2 = float(input("Enter the diameter of other pizza: "))
pizza_1 = float(input("Enter the price of the first pizza: "))
pizza_2 = float(input("Enter the price of the other pizza: "))
pizza_per_m2_1 = pizza_per_m2(diam_1,pizza_1)
pizza_per_m2_2 = pizza_per_m2(diam_2,pizza_2)

if pizza_per_m2_1 < pizza_per_m2_2:
    print("The first pizza has better unit price!")
elif pizza_per_m2_1 > pizza_per_m2_2:
    print("The other pizza has better unit price!")
