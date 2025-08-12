friends = ['Sarah', 'John', 'Hannah', 'Dave']

for i in range(0, len(friends)):
    print("Hello, " + friends[i] + '!')

print("             ")

# for iterating directly over items
for friend in friends:
    print("Hello, " + friend + '!')

print("             ")

#using the f=strong method
for friend in friends:
    print(f"Hello, {friend}!")
