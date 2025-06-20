while True:
    user_text = input("Write the 'text' you want to encrypt\n").lower()
    if all(c.isalpha() or c.isspace() for c in user_text):
        break
    else:
        print("Only words and chars")

while True:
    user_shift = input("Keep it a secrete! how much is the shifting key?\n")
    if user_shift.isdigit():
        user_shift = int(user_shift)
        break
    else:
        print("The encrtyp key must be a number") 

alphabet = '' # do not write manually
a, z = ord("a"), ord("z")
for char in range(a, z+1):
    char = chr(char)
    alphabet += char

def ceaser(text, key):
    fullenctext = ''
    for char in user_text.lower():
        if char == ' ':
            fullenctext += char
        else:
            index = alphabet.find(char)
            new_index = (index + user_shift) % len(alphabet)
            fullenctext += alphabet[new_index]
    print(f"orginial text: {user_text}")
    print(f"full massege: {fullenctext}")


ceaser(user_text, user_shift)

