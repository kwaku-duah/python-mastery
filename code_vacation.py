dreams = {}

interested = True

while interested:
    name = input('If you could visit one place where will you go ')
    answer = input('\nEnter your place ')

    dreams[name] = answer

    print('\nWanna move to the next person" ')
    go_again = input('Quit or Continue ')
    if go_again == 'no':
        interested = False

for key, value in dreams.items():
    print(f"\n{key}")
    print(f"\n{value}")

