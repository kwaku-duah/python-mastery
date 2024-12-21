# to modify a list while you work through it, use while loop
unconfirmed_users = ['alice','brian','candace']

confirmed_users = []

while unconfirmed_users:
        current_user = unconfirmed_users.pop()
        print(f'\nYou are now verified, {current_user.title()}')
        confirmed_users.append(current_user)

print(f"\nListing confirmed users")
for confirmed_user in confirmed_users:
    print(f"{confirmed_user} is now verified")