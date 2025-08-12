friends = ['Sarah', 'John', 'Hannah', 'Dave']

for i in range(0, len(friends)):
    print("Hello, " + friends[i] + '!')

print("             ")

for friend in friends:
    print("Hello, " + friend + '!')

print("             ")

for friend in friends:
    print(f"Hello, {friend}!")
