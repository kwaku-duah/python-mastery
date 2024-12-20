#omitting the else block to guard against malicious code
age = 66
if age < 4:
    price = 0
elif age < 18:
    price = 20
elif age < 65:
    price = 40
elif age >=65:
    price = 20
print(f"Your admission fee based on your age is {price}")