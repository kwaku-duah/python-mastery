# looping through a dicts keys in a particular order sort method
favorite_languages = {
    'jen': 'python',
    'kalderon': 'c++',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}
# sorts a copy of the dictionary
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll")