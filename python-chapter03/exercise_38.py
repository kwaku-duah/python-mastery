locations = ["Bali", "Addis Ababa", "Moscow", "Berlin", "Tonga"]

# print the list in original order
print(locations)

# print using sorted function in alphabetical order
print("Sorted Locations using sorted function",sorted(locations))

#proof that list is in its original order by reprinting it
print(locations)

# sorted function to print list in reverse-alphabetical order
print(sorted(locations,reverse=True))

# proof that list is still in its original order
print(locations)

# reverse method to change order of a list
locations.reverse()
print(locations)

# reversing the list again to show it is back to its original order
locations.reverse()
print(locations)

# use sort method to show that the list has been modified permanently
locations.sort()
print(locations)

# use sort to reverse your list so it is sorted in alphabetical order
locations.sort(reverse=True)
print(locations)
