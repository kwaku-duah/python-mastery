requested_toppings = ['chicken']

# first check to see if it is empty
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding your {requested_topping} topping")
    print('\nFInished making your pizza')
else:
    print('Are you sure you want a plain pizza?')