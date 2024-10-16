'''

#1
from random import randint

dice_num = int(input("Enter a number of dice: "))
dice_sum = 0

for i in range (dice_num):
    temp_num = randint(1,6)
    print(temp_num)
    dice_sum += temp_num
print(dice_sum)


#2

user_num = input("Enter a number or an empty string to stop: ")
num_list = []

while user_num != "":
    user_num = float(user_num)
    num_list.append(user_num)
    user_num = input("Enter a number or an empty string to stop: ")
num_list.sort(reverse=True)
print(num_list)
for i in range(5):
    print(num_list[i])


'''


#3

num = int(input("Enter a number"))
if num == 1:
    print("It is 1 which is neither prime nor composite.")
elif num > 1:
    for i in range(2,num):
        if num%i == 0:
            check = True
            break
        else:
            check = False
    if check == True:
        print("Its a composite number")
    else:
        print("Its a prime number")
else:
    print("Negative numbers cant be prime numbers")



#4

cities = []
for i in range(5):
    city = input("Enter the name of a city,")
    cities.append(city)
for i in cities:
    print(i)




