#using the str.count method to check whether a string contains a specific substring

example_string = "Well Well Well, what do we have here?"

print(example_string.count('Well'))

# using the str.find method to check whether a string contains a specific substring
# if greater than 0, it exists

print(example_string.find('Well', 0, len(example_string)))


# using the str.index method to check whether a string contains a specific substring
# if greater than 0, it exists, otherwise we get ValueError


print(example_string.index('Well', 0, len(example_string)))

