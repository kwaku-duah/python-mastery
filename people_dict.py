peoples = {
    'kduah':{
        'first': 'kwaku',
        'last': 'duah',
        'location': 'tema'
    },

    'tankamah': {
        'first': 'theophilus',
        'last': 'ankamah',
        'location': 'sefwi'
    },

    'lkoranteng': {
        'first': 'Lois',
        'last': 'Koranteng',
        'location': 'suhum'
    }

}

for people, details in peoples.items():
    print(f"\n{people.title()}")
    full_name = f"{details['first']} {details['last']}"
    location = f"{details['location']}"

    print(f"{full_name.title()} \n{location.title()}")