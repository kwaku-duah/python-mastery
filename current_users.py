current_users = ['kwaku','duah','antwi','admin','gyamfua']

new_users = ['frank','irene','kwame','kalderon','gyamfua']

available_already = current_users[:]

# loop over the new_users, to see if any form of it exists in the current users
for new_user in new_users:
    if new_user.lower() in available_already:
        print(f"Your {new_user} username is taken choose a different name")
    else:
        print(f"Your {new_user} username is all clear!")



