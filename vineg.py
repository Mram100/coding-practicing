# 1. get direction
while True:
    user_direction = int(input("choose a direction: "))
    if user_direction:
        break
    print("Choose from the list!")

# 2. get text

while True:
    if user_direction >= 1:
        text = input("Write the text you want to Encrypt: ")
    else:
        text = input("Write the text you want to Decrypt: ")
    if all(c.isalpha()  or c.isspace() for c in text):
        break
    print("Please enter a text! ")
# 3. get key
while True:
    short_key = input("Write the encryption key: ")
    if short_key.isalpha():
        break
    print("Please enter a text! ")

def vinegere(user_text, user_key, user_direction):
    key = ''
    key_index = 0
    for char in user_text:
        if char == ' ':
            key += ' '
        else:
            key += user_key[key_index % len(user_key)]
            key_index += 1

    alphabet = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))

    encrypted_text = ''
    for text_char, key_char in zip(user_text.lower(), key.lower()):
        if text_char == ' ':
            encrypted_text += ' '
        else:
            text_index = alphabet.find(text_char)
            shift_index = alphabet.find(key_char)

            if user_direction >= 1:
                new_index = (text_index + shift_index) % len(alphabet)
            elif user_direction <= 1:
                new_index = (text_index - shift_index) % len(alphabet)

            encrypted_text += alphabet[new_index]

    return encrypted_text

result = vinegere(text, short_key, user_direction)

print(result)
