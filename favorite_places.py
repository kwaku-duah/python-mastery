favorite_places = {
    'ken': {
        'full_name': 'ken nedy',
        'place': 'afuom gardens',
        'fav_number': [23, 45, 56]
    },

    'ben': {
        'full_name': 'ben jamin',
        'place': 'mount heron',
        'fav_number': [45, 56, 89,67]
    },

    'deg': {
        'full_name': 'deg raft',
        'place': 'mount afadjato',
        'fav_number':[34, 56, 78, 93]
    }
}

for person, info in favorite_places.items():
    print(f"\n{person.title()}")
    name_favs = f"{info['full_name'].title()} and {info['place'].title()} "

    for favorite in info['fav_number']:
        print(favorite, end=' ')
