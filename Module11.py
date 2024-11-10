'''
#1

class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(self.name)
class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"The book {self.name}, written by {self.author}, has {self.page_count} pages")
class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"The book {self.name}, edited by {self.chief_editor}")

magazine1 = Magazine("Donald Duck", "Aki Hyyppä")
magazine1.print_information()

book1 = Book("Compartment No. 6", "Rosa Liksom", 192)
book1.print_information()
'''

#2

import random

class Car:
    def __init__(self, registration_num, max_speed):
        self.registration_num = registration_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def print_info(self):
        print(f"Registration number:{self.registration_num}\nMaximum speed:{self.max_speed}")

    def accelerate(self, change_speed):
        self.current_speed += change_speed
        if self.current_speed < 0 or self.current_speed > self.max_speed:
            if self.current_speed < 0:
                self.current_speed = 0
            elif self.current_speed > self.max_speed:
                self.current_speed = self.max_speed
        else:
            pass
        return self.current_speed

    def drive(self, hours):
        self.travelled_distance += hours * self.current_speed
        return self.travelled_distance

class Race(Car):

    def __init__(self, name, distance, car_num):
        self.name = name
        self.distance = distance
        self.car_num = car_num
        self.car_list = []
        for c in range(0, car_num):
            regestration_number = "ABC-" + str(c)
            max_speed = random.randint(100, 201)
            self.car_list.append(Car(regestration_number, max_speed))

    def hour_passes(self):
         for car in self.car_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
            print(f"{car.registration_num:<15} {car.max_speed:<23} {car.current_speed:<20} {car.travelled_distance:<25}")


    def print_status(self):
        print("{:<10} {:<20} {:<25} {:<20}".format("Reg Num", "Max Speed (km/h)", "Current Speed (km/h)", "Distance (km)"))

    def race_finished(self):
        for car in self.car_list:
            if car.travelled_distance >= self.distance:
                return True

class Electricar(Car):
    def __init__(self,battery_capacity,registration_num,max_speed):
        super().__init__(registration_num,max_speed)
        self.battery_capacity = battery_capacity
        self.current_speed = 0
        self.travelled_distance = 0


class Gasolinecar(Car):
    def __init__(self,tank_capacity,registration_num,max_speed):
        super().__init__(registration_num,max_speed)
        self.tank_capacity = tank_capacity
        self.current_speed = 0
        self.travelled_distance = 0

cars=[]
cars.append(Electricar("52.5 kw/h","ABC-15",180))
cars.append(Gasolinecar("32.3 l","ACD-15", 165))
hours=0

while hours<=3:
    for car in cars:
        car.accelerate(random.randint(0,15))
        car.drive(1)
    hours+=1
print("Registration Number","Maximum Speed", "Current Speed","Travelled Distance",sep="|")
for car in cars:
    car.print_info()