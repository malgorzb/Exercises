'''
#1

class Car:
    def __init__(self,reg_num,max_speed,curr_speed = 0,travelled_dist = 0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.curr_speed = curr_speed
        self.travelled_dist = travelled_dist

    def print_deets(self):
        print("The registration number:",self.reg_num," \nThe maximum speed of the car =",self.max_speed,"km/hr\nThe current speed of the car =",self.curr_speed,"km/hr\nThe distance the car has travelled =",self.travelled_dist,"km")
car1 = Car("ABC-123", 142)
car1.print_deets()

#2

class Car:
    def __init__(self,reg_num,max_speed,curr_speed = 0,travelled_dist = 0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.curr_speed = curr_speed
        self.travelled_dist = travelled_dist
    def accelarate(self,change):
        if self.curr_speed+change>self.max_speed:
            print("Exceeds maximum speed of the car hence speed becomes maximum")
            self.curr_speed = self.max_speed
            print(self.curr_speed)
        elif self.curr_speed+change<0:
            print("Negative speed is not possible hence speed becomes 0")
            self.curr_speed=0
            print(self.curr_speed)
        else:
            self.curr_speed=self.curr_speed+change
            print(self.curr_speed)
    def print_deets(self):
        print("The registration number:",self.reg_num," \nThe maximum speed of the car =",self.max_speed,"km/hr\nThe current speed of the car =",self.curr_speed,"km/hr\nThe distance the car has travelled =",self.travelled_dist,"km")

car1 = Car("ABC-123", 142)
car1.print_deets()
while True:
    choice=int(input("Enter 1 if you want to accelerate, Enter 2 if not"))
    if choice==1:
        change=int(input("How much speed do you want to change(Please enter in km/hr)"))
        car1.accelarate(change)
    elif choice==2:
        break

'''

#3

class Car:
    def __init__(self,reg_num,max_speed,curr_speed = 0,travelled_dist = 2000):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.curr_speed = curr_speed
        self.travelled_dist = travelled_dist
    def accelarate(self,change):
        if self.curr_speed+change>self.max_speed:
            print("Exceeds maximum speed of the car hence speed becomes maximum")
            self.curr_speed = self.max_speed
            print(self.curr_speed)
        elif self.curr_speed+change<0:
            print("Negative speed is not possible hence speed becomes 0")
            self.curr_speed=0
            print(self.curr_speed)
        else:
            self.curr_speed=self.curr_speed+change
            print(self.curr_speed)
    def drive(self,time):
        self.travelled_dist=self.travelled_dist+(self.curr_speed*time)
        print(f"The car has now travelled {self.travelled_dist}")

    def print_deets(self):
        print("The registration number:",self.reg_num," \nThe maximum speed of the car =",self.max_speed,"km/hr\nThe current speed of the car =",self.curr_speed,"km/hr\nThe distance the car has travelled =",self.travelled_dist,"km")

car1 = Car("ABC-123", 142)
car1.print_deets()
while True:
    choice=int(input("Enter 1 if you want to accelerate, Enter 2 if not"))
    if choice==1:
        change=int(input("How much speed do you want to change(Please enter in km/hr)"))
        car1.accelarate(change)
    elif choice==2:
        break
car1.drive(1.5)