
# extracts region by slicing twice
def extract_region(locale):
    slice_off_UTF = locale.split(".")
    slice_off_language = slice_off_UTF[0].split("_")
    return slice_off_language[1]

# extracts region by slicing twice in same line
def extract_region2(locale2):
    return locale2.split(".")[0].split("_")[1]

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR
print(extract_region2('bababab_TH.UTFUUUU-16'))   # KR