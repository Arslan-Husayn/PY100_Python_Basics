def greet(language_code):
    if language_code == 'en':
        return "Hi!"
    if language_code == 'fr':
        return "Salut!"
    if language_code == 'pt':
        return "Olá!"
    else:
        return "Not a supported code!"



print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!