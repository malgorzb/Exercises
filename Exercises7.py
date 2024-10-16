'''
#1

def the_season (month):

    season = ("spring", "summer", "autumn", "winter")

    if month in [12, 1, 2]:
        return season[3]
    elif month in [3, 4, 5]:
        return season[0]
    elif month in [6, 7, 8]:
        return season[1]
    elif month in [9, 10, 11]:
        return season[2]
    else:
        return None

num_of_themonth = int(input("Enter the number of the month (1-12): "))
season = the_season(num_of_themonth)
print(f"The season is {season}, because the month is {num_of_themonth}")



#2

name = 0
lst = set()
while name != "":
    name = input("Enter a name,")
    if name in lst:
        print("Existing name")
    elif name == "":
        break
    else:
        lst.add(name)
        print("New name")
for i in lst:
    print(i)

'''

#3

choice = True
aiports = {}

while choice != 0:
    choice = int(input("Enter '1' if you want to enter new airport data, "
                       "\n'2' if you want to fetch information of an existing airport "
                       "\nand '0' if you want to quit \n:"))
    if choice == 1:
        ICAO_code = input("Enter the ICAO code: ")
        airport_name = input("Enter the name of the airport: ")
        aiports[ICAO_code] = airport_name
    if choice == 2:
        ICAO_code = input("Enter the ICAO code of the airport you want to search for: ")
        print(aiports[ICAO_code],"is the name of the airport")
    if choice == 3:
        break
