motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# modifying a list in python
motorcycles[0] = 'durati'
print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

# emtpy list filling

cars = []
cars.append('toyoto')
cars.append('tractor')
cars.append('tesla')
print(cars)

cars.insert(0, "cybertruck")
print(cars)

del cars[0]
print(cars)

# remove an element and still be able to use it, pop()
popped_car = cars.pop()
print(popped_car)