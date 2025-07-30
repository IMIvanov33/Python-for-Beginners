msg = input(">")
words = msg.split(' ')
emoji = {
    ":)": "😊",
    ":(":  "☹️"  # you can map here all the emoji's ... yeah right :D
}
output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)
