favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n {name.title()} favorite language is"
        " listed below: ")
        for language in languages:
            print(f"\n{language.title()}")
    else:
         print(f"\n {name.title()} favorite languages are"
        " listed below: ")
         for language in languages:
            print(f"\n{language.title()}")
    