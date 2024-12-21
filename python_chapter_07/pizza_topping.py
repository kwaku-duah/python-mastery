prompt = '\nEnter a topping you may want to add to your pizza '
prompt += '\nEnter "quit" to exit the program '

pizza_topping = ""
while pizza_topping != 'quit':
    pizza_topping = input(prompt)

    if pizza_topping == 'quit':
        break
    else:
        print(f"\n{pizza_topping} topping will be added to your pizza ")


