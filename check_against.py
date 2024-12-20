available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni','pineapple','extra cheese']

requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"We are adding your {requested_topping} ")
    else:
        print(f"Sorry your requested {requested_topping} no dey")
print("\nFinished making your pizza!")