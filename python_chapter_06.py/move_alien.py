alien_o = {'x-position': 0, 'y-position':25, 'speed':'medium'}
print(f"original position: {alien_o['x-position']}")

alien_o['speed'] = 'fast'
# move alien to the right - determine how far to move alien due to current speed
if alien_o['speed'] == 'slow':
    x_increment = 1
elif alien_o['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3
# new position would be a sum of current and new increment
alien_o['x-position'] = alien_o['x-position'] + x_increment

print(f"The new position for the alien is {alien_o['x-position']}")

