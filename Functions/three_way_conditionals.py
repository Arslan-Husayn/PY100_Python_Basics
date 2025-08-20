def compare_by_length(word1, word2):
    if len(word1) > len(word2):
        return 1
    if len(word1) == len(word2):
        return 0
    if len(word1) < len(word2):
        return -1


print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity'))      #  1
print(compare_by_length('humor', 'grace'))          #  0


def compare_by_length2(word1, word2):
    if len(word1) > len(word2):
        return 1
    elif len(word1) == len(word2):
        return 0
    else:
        return -1


print(compare_by_length2('patience', 'perseverance')) # -1
print(compare_by_length2('strength', 'dignity'))      #  1
print(compare_by_length2('humor', 'grace'))          #  0