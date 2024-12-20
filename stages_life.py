age = 23
if age < 2:
    message = 'baby'
elif age < 4:
    message = 'toddler'
elif age < 13:
    message = 'kid'
elif age < 20:
    message = 'teenager'
elif age < 65:
    message = 'adult'
elif age >= 65:
    message = 'elder'
print(f"You are a/an {message}")