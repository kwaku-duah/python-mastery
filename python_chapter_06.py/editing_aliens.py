aliens = []

for alien_number in range(30):
    new_aliens = {'color': 'yellow', 'points':5, 'speed':15}

    aliens.append(new_aliens)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
print(aliens[:5])

        