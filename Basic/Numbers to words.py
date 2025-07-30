phone = input("Phone:")
number_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero",
}
for char in phone:
    if char in number_mapping:
        print(number_mapping[char], end=" ")
    else:
        print("!", end=" ")  # For characters not in the mapping
