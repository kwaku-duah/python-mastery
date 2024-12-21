sandwich_orders = ['vegies','fluffy', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print('Oops Pastrami is finished')
while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    
    in_use = sandwich_orders.pop()
    finished_sandwiches.append(in_use)

for sandwich in finished_sandwiches:
    print(f'\nI made your {sandwich} sandwich')