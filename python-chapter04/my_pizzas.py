pizzas = ['pepperoni', 'chicken', 'beef']

friend_pizzas = pizzas[:]

pizzas.append("cucumber")
friend_pizzas.append('vegetable-pizza')
print(pizzas)
print(friend_pizzas)


for pizza in pizzas:
    print(f"My favorite pizzas are: {pizza}\n")

for friend_pizza in friend_pizzas:
    print(f"My friends favorite pizzas are: {friend_pizza}")