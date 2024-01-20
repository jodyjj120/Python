class Vehicle :

    def __init__(self, milage, cost) :

        self.milage = milage
        self.cost = cost


    def show_details(self) :
        print("i am a vehicle")
        print("the milage of the car is :", self.milage)
        print("the cost of the car is :", self.cost)




class Car(Vehicle) :

    def show_car_details(self) :
        print("i am a car")

c1 = Car(600, 90000)

c1.show_details()

c1.show_car_details()


