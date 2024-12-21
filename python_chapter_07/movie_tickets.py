prompt = '\nEnter your age '
prompt += '\nEnter 0 to exit the program '

age = ''
print(age)

while age != 0:
    age = int(input(prompt))

    if age == 0:
        break
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    elif age > 12:
        price = 15

    print(f"\nFor your age {age} your ticket price is {price}")