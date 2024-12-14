# lists are represented with square brackets, sets of information
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

# accessing elements in a list
print(bicycles[0])

# possible to apply methods on an element in a list
print(bicycles[0].title())

# indexing in python
print(bicycles[1])
print(bicycles[3])

# returninng last item in a list
print(bicycles[-1])

# composing a message
message = f"My first bicycle was on a {bicycles[0].title()}."
print(message)
