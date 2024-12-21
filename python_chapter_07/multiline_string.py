prompt = "If you share your name, we can personalize the messages you see"

# the += operator takes what was assigned to prompt variable and adds the new assignage to its end
prompt += '\nWhat is your first name? '

name  = input(prompt)
print(f"\nHello, {name}")