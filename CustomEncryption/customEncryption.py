custom_key = {
    'er4r': 'a',
    'qt45': 'b',
    '32vs': 'c',
    '23rg': 'd',
    'sdg4': 'e',
    'ef43': 'f',
    'btht': 'g',
    '1edd': 'h',
    '5yhb': 'i',
    '9rs2': 'j',
    'sdgg': 'l',
    'yjuy': 'm',
    'tjty': 'n',
    'thju': 'o',
    '2e33': 'k',
    'ujuf': 'p',
    'fdjj': 'q',
    'ihvf': 'r',
    'xzsv': 's',
    '3fgr': 't',
    'eger': 'u',
    '65uj': 'v',
    '78ne': 'w',
    '1ws2': 'x',
    '45r2': 'y',
    '23ax': 'z',
    'hyr4': ' '
}

def encode(secret):
    newString = ''
    for letter in secret:
        for key in custom_key:
            if custom_key[key] == letter:
                newString += key
    return newString

def decode(secret):
    # Decode the secret based on the custom_key and return cleartext
    newString = ''
    constant = 0
    for loopNumber in range(len(secret) // 4):
        for key in custom_key:
            if key == secret[constant:constant + 4]:
                newString += custom_key[key]
                constant += 4
    return newString

# For applications manager

encodeOrDecode = input("Would you like to encode or decode a secret? ")
if encodeOrDecode == "encode":
    print(' ')
    secret = input("Enter the secret to encode: ")
    print(' ')
    print("Encoded Secret:")
    print(encode(secret))
elif encodeOrDecode == "decode":
    print(' ')
    secret = input("Enter the secret to decode: ")
    print(' ')
    print("Decoded Secret:")
    print(decode(secret))