my_foods = ['pizza', 'falafel', 'carrot cake']

# copying an entire list, you simply use : which references the start to end
friends_food = my_foods[:]

print(my_foods)
print("He is evil", friends_food)

my_foods.append('Banku')
friends_food.append('Tilapia')
print(my_foods,friends_food)