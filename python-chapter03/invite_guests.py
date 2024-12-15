names = ["Jesus", "Hitler", "Carthaginian"]
print(f"Hello, {names[0]}, welcome to the first supper with the kalderon")
print(f"Hello, {names[1]}, the time is now")
print(f"Hello, {names[2]},  war cometh, return to beat the italians")

print(f"Hello all, {names[0]} cannot make it, Paul Atreidas has invited him to the purgasoth")

names[0] = 'Judas Iscariot'
print(f"Hello, {names[0]} evil one is returned")
print(f"Hello, {names[1]} seat is certain")
print(f"Hello, {names[2]} great general arise")

print("More table is in now, more people are now gonna be invited over!")

names.insert(0, "Kwaku Duah")
names.insert(2, 'Odieba Kalderon')
names.append('Bullock')

print(f"Hello {names[0]} welcome!")
print(f"Hello {names[1]} welcome!")
print(f"Hello {names[2]} welcome!")
print(f"Hello {names[3]} welcome!")
print(f"Hello {names[4]} welcome!")
print(f"Hello {names[5]} welcome!")

print("Sorry an unforseen circumstance is up, I can invite only two high priority individuals!")
names.pop(0)
names.pop(1)
names.pop(2)
names.pop()

print(names)

print(f"Hello, {names[0]} and {names[1]} yet remain invited!")
del names[0]
del names[0]

# not advisable better using slice
del names[0:2]


print('Now we are waiting for an empty string', names)