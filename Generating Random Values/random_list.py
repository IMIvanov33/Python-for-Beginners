import random  # This loads the random module so we can use random functions

# We create a list of names called "members"
members = ['Josh', 'Ivan', 'Bobi', 'Georgi']

# Pick one random name from the list and save it in the variable "lider"
lider = random.choice(members)

# Print the selected name
print(lider)
