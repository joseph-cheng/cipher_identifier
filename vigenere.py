def encrypt_vigenere(pt, key):
    final = []

    length = len(key)
    for it, char in enumerate(pt):
        final.append( chr((ord(char)-65 + ord(key[it%length])-65)%26 + 65))

    return final

