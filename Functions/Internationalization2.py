# extracts the language
def extract_language(locale):
    extract_lan = locale.split("_")
    return extract_lan[0]

# extracts the region
def extract_region(locale):
    return locale.split(".")[0].split("_")[1]

def greet(language_code):
    if language_code == 'en':
        return "Hi!"
    if language_code == 'fr':
        return "Salut!"
    if language_code == 'pt':
        return "Olá!"
    else:
        return "Not a supported code!"

def local_greet(locale):
    region = extract_region(locale)
    language = extract_language(locale)
    if region == "US" and language == "en":
        return "Hey!"
    elif region == "GB" and language == "en":
        return "Hello!"
    elif region == "AU" and language == "en":
        return "Howdy!"
    else:
        return greet(language)
   




print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!