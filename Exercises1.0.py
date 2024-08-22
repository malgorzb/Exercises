
#E1

print("Hello, May Brzozka!")

#E2
#1
name = input('Enter your name: ')
print("Hello, ", name ,"!")

#2
import math
rds = float(input("Enter a RDS: "))
area = math.pi * (rds ** 2)

print(f"Your RDS is, {rds}, and area is, {area:.2f}")

#3
length = float(input("Enter a length: "))
width = float(input("Enter a width: "))
print(f"Perimeter of your rectangle is {(length + width) * 2}")
print(f"Area of your rectangle is {(length * width)}")

#4
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
sum = num1 + num2 + num3
product = num1 * num2 * num3
average = sum / product
print("The sum is", sum ,", The product is", product, ", The average is", average)

#5
talentTopound = 20
poundTolot = 32
lotTograms = 13.3

talent = float(input("Enter Talents"))
pound = float(input("Enter Pounds"))
lot = float(input("Enter Lots"))

totallots = (talent * talentTopound * poundTolot) + (pound * poundTolot) + lot
totalgrams = totallots * lotTograms

kilograms = int(totalgrams // 1000)
grams = totalgrams % 1000

print("The total mass in kilograms is", kilograms)
print("The total mass in grams is", grams)


#6
from random import randint

code1_num1 = randint(0, 9)
code1_num2 = randint(0, 9)
code1_num3 = randint(0, 9)
code1 = (f" {code1_num1} {code1_num2} {code1_num3} ")
print(code1)

code2_num1 = randint(0, 6)
code2_num2 = randint(0, 6)
code2_num3 = randint(0, 6)
code2_num4 = randint(0, 6)
code2 = (f" {code2_num1} {code2_num2} {code2_num3} {code2_num4} ")
print(code2)


