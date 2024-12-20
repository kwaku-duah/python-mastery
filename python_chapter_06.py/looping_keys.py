favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

# using the keys method to list only the keys
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil','sarah']

for name in favorite_languages.keys():
    print(f"\nHi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you like {language}")

# find out if someone is missing using keys method
if 'erin' not in favorite_languages.keys():
    print("Please take the poll")