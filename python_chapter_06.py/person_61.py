person = {'firstName':'Kwaku', 'lastName':'Duah','city':'casper','age':34}

favorite_numbers = {
    'jen':13,
    'kwaku':45,
    'gemini':67,
    'eddy':17,
    'akum':31
}

for name in favorite_numbers:
    corresponding_value = favorite_numbers[name]
    print(f"{name} favorite number is {corresponding_value}")
