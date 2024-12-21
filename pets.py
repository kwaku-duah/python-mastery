pets = {
    'pet_1': {
        'owners_name': 'krisha',
        'type': 'german shepherd'
    },

    'pet_2': {
        'owners_name': 'lord',
        'type': 'cat'
    }
}

for pet, info in pets.items():
    print(f"{pet}")
    owner = f"{info['owners_name']}"
    type = f"{info['type']}"

    print(f"{owner} and {type}")