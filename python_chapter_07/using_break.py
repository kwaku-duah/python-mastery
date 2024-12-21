prompt = '\nTell me something and I will repeat it back to you '

prompt += '\nEnter "quit" to quit this program '

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"\nBest {city}")