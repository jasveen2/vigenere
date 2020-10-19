import sys # for args

action = sys.argv[1] # shifted by 1 because sys was taking vigenere.py as an action
text = sys.argv[2]
key = sys.argv[3]

def vigenere(text, key, encode):
    text = text.lower()
    key = key.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if len(text) > len(key): # repeats key to length of text
        repeats = (len(text) // len(key)) + 1 # max num of repeats
        key2 = key * repeats
        key = key2[:len(text)] # gets rid of extra letters
    encoded = ''
    index = 0 # counter for index in key
    for letter in text:
        keyindex = alphabet.index(key[index])
        if encode != True: #if decode then subtract key index in alphabet instead of add
            keyindex *= -1 
        newindex = alphabet.index(letter) + keyindex
        index += 1
        encoded += alphabet[newindex % 26] # mod so it wraps around the alphabet
    return encoded

if sys.argv[1] == 'encode':
    print(vigenere(text, key, True))
else:
    print(vigenere(text, key, False))
