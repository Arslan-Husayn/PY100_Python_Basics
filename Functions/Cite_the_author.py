
def cite(author, quote):
    statement = str(author) + " said: " + str(quote)
    return print(statement)


cite('Bruce Eckel', '"Python is executable pseudocode."')
# Bruce Eckel said: "Python is executable pseudocode."


#version 2

def cite2(author, quote):
    print(f"{author} said: {quote}")
    


cite2('Bruce Eckel', '"Python is executable pseudocode."')