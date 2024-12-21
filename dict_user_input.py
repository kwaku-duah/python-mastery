# creating a dictionary
responses = {}

polling_active = True
while polling_active:
    name = input('What is your name? ')
    response = input('What is your favorite food? ')

    responses[name] = response
    

    repeat = input('Is there anyone else who wants to take the test? ')
    if repeat == 'no':
        polling_active = False
    
print(f'\n--- Poll Results is complete ----')
for name , response in responses.items():
    print(f"{name} would like to climb {response}")