def encrypt_substitution(pt, key):
    return [key[ord(char)-65] for char in pt]    
