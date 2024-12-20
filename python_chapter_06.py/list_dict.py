# storing a list in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print(f"The crust {pizza['crust']} and "
    "with following pizza")


for topping in pizza['toppings']:
    print(f"{topping} topping")
