# removing an item from a list without knowing the value
motorcycles = ["honda", 'yamaha', "suzuki", "ducati"]
motorcycles.remove("ducati")
print(motorcycles)

too_slow = 'honda'
motorcycles.remove(too_slow)
print(motorcycles)
print(f"\nA {too_slow.title()} is too slow for me.")