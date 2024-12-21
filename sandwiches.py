sandwich_orders = ['vegies','fluffy', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    
    in_use = sandwich_orders.pop()
    finished_sandwiches.append(in_use)

for sandwich in finished_sandwiches:
    print(f'\nI made your {sandwich} sandwich')