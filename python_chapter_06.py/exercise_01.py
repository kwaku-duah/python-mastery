rivers = {'nile':'egypt','euphrates':'Iraq','offin':'ghana'}

for river,place in rivers.items():
    print(f"the {river} runs through ")
    print(f"{place}")

for river in rivers.keys():
    print(f"{river}")

for river in set(rivers.values()):
    print(f"{river}")