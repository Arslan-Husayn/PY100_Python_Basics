
# extracts first two letters of locale, representing the language
def extract_language(locale):
    extract = locale[0:2]
    return extract

# extracts first two letters of locale, using partition
def extract_language2(locale2):
    extract2 = locale2.partition("_")
    return extract2 [0]

# using a string split
def extract_language3(locale3):
    extract3 = locale3.split("_")
    return extract3[0]

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko
print(extract_language3('fil_PH.UTF-8'))     # ko