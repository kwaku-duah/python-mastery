mountains = ["mountain Afadjato", "Ntensere Mountain", "Buoho Mountain", "Mississippi Mountain"]

# sorted function temporarily alphabetically
temp_alpha = sorted(mountains)
print(temp_alpha)

# reverse alphabetical sorted temporarily
temp_reverse_sort = sorted(mountains,reverse=True)
print(temp_reverse_sort)

# use sort to permanently alter a list
mountains.sort()
print(mountains)

# reverse permanence sort
mountains.sort(reverse=True)
print(mountains)

# getting the length of a list
number_invitees = len(mountains)
print(number_invitees)
