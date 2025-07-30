weight = int(input('Weight: '))
unit = input('(L)bs or (K)g? ')
if unit.upper() == "L":
    converted_weight = weight * 0.45
    print(f"You are {converted_weight} kg")
else:
    converted_weight = weight / 0.45
    print(f"You are {converted_weight} lbs")
