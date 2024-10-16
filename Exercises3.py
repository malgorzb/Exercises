
#E3

#1

length = float(input('Enter lenght of zander in centimeters: '))
sizelimit = 42
if length < sizelimit:
    difference = sizelimit - length
    print(f"Release the fish back into the lake, because it is {difference} centimeters too small.")
else:
    print("The fish bigger than the size limit, you can keep it.")


#2

CabinClass = input("Enter the cabin class of a cruise ship (LUX, A, B, C): ")
if CabinClass == "LUX":
    print(f"Upper-deck cabin with a balcony.")
elif CabinClass == "A":
    print(f"Above the car deck, equipped with a window.")
elif CabinClass == "B":
    print(f"Windowless cabin above the car deck.")
elif CabinClass == "C":
    print(f"Windowless cabin below the car deck.")
else:
    print(f"Invalid cabin class.")


#3

gender = input("Enter your gender (female or male): ")
hemoglobin = float(input("Enter your hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("Hemoglobin value is low.")
    elif 117 <= hemoglobin <= 155:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
elif gender == "male":
    if hemoglobin < 134:
        print("Hemoglobin value is low.")
    elif 134 <= hemoglobin <= 167:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
else:
    print("Invalid gender. Please enter 'female' or 'male'.")


#4

year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("It is a leap year.")
else:
    print("It isn't a leap year.")


#OR


if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("It is a leap year.")
        else:
            print("It isn't a leap year.")
    else:
        print("It is a leap year.")
else:
    print("It isn't a leap year.")
