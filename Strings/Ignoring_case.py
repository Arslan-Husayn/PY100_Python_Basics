name = 'Roger'
string1 = "RoGeR"
string2 = "Dave"

if name.lower() == string1.lower():
    print(True)
else:
    print(False)

if name.lower() == string2.lower():
    print(True)
else:
    print(False)   


# casefold way

print(name.casefold() == string1.casefold())
print(name.casefold() == string2.casefold())