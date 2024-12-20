favorite_language = {
    'jen': "python",
    'kennedy': "c",
    'roland': 'js',
    'akwasi': 'c++',
    'odie': 'python'
}
print('These are the languages people chose')

for language in favorite_language.values():
    print(language.upper())

# return unique lists
# use a set, a unique collection of values ensuring no repeatition

for language in set(favorite_language.values()):
    print(language)
