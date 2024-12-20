# using keys can be problematic, if the key does not exist, it wiill fling an error
# so we will use GET() method

alien_0 = {'color': 'green','speed':5}

# demonstrated here
# alien_0['points']
# print(alien_0)

# get method
point_value = alien_0.get('points', 'No value assigned')
print(point_value)
