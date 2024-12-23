# you can nest a dictionary in a dictionary

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        "location": 'princeton'
    },

    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['location']}"

    print(f"{full_name.title()} \n{location.title()}")