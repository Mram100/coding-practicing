# we need a text to encrypt
text = "Hello zaira"
# we need the key of the encrypt
key = "python"
# we need the alphabet to manipulate
alphabet = '' # do not write manually
a, z = ord("a"), ord("z")
for char in range(a, z+1):
    char = chr(char)
    alphabet += char

# We need to repeat the key
rep_key = ''
for i in range(len(text)):
    rep_key += key[i % len(key)]

enc_text = ''
# iterate through text and to find the index and calculat the index:
for text_char, key_char in zip(text, rep_key):
    text_index = alphabet.find(text_char)
    key_index = alphabet.find(key_char)

    # calc the new index of each letter
    new_index = (text_index + key_index) % len(alphabet)
    enc_text += alphabet[new_index]

print(enc_text)
    


# outcomes:
# reviewed the cipher.py file and updated it
# practiced and tried to figur out how the vinegere works
# learnt how to find the index myself

