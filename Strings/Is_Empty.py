def is_empty(string):
    if len(string) == 0:
        return True
    else:
        return False

# returning the boolean
def is_empty2(string):
    return len(string) == 0 


print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

print(is_empty2('mars'))  # False
print(is_empty2('  '))    # False
print(is_empty2(''))      # True