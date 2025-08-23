def is_empty_or_blank(string):
    return len(string) == 0 or string.isspace()
        
# using strip

def is_empty_or_blank2(string):
    return len(string.strip()) == 0
    




print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True


print(is_empty_or_blank2('mars'))  # False
print(is_empty_or_blank2('  '))    # True
print(is_empty_or_blank2(''))      # True