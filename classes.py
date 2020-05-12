class Car:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Fiat(Car):
    def turn_engine(self):
        print(f"Fiat {self.name} - *врум-врум*")

    def auto_park(self):
        print(f"Fiat {self.name} паркует сама себя")


class Toyota(Car):
    def turn_engine(self):
        print(f"Toyota {self.name} - *дрынь-дрынь*")

    def auto_park(self):
        print(f"Toyota {self.name} идёт парковаться")


italian_car = Fiat("Model 3")
japanese_car = Toyota("Supra 10")
my_objects = [italian_car, japanese_car]
for o in my_objects:
    print(o)
    o.turn_engine()
    o.auto_park()
