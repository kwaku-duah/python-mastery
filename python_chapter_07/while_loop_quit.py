prompt = '\nTell me something and I will repeat it back to you '

prompt += '\nEnter "quit" to quit this program '

message = ''

while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

# it keeps on running as long as the while condition is true
