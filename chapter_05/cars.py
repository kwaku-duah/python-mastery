# perfect demonstration of an if loop in python, it is used to solve a problem
cars = ['audi','bmw','subaru','toyota']

# loop to go through the list
for car in cars:
    #if a  certain condition is met, we define an output
    if car == 'bmw':
        print(car.upper())
    # else define an output
    else:
        print(car.title())