class CarRent():
def __init__(self, model, engine, km):
self.model = model
self.engine = engine
self.km = km

def km_degistir(self, km):
self.km += km

car1 = CarRent("civic", "gas", 1000)
print(car1.km)
print("araba 10 km ilerledi")
car1.km_degistir(10)
print(car1.km)
