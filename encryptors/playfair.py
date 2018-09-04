import string

def encrypt_playfair(pt, key):
    seen = set()
    square = [char for char in key if not (char in seen or seen.add(char))] + [char for char in string.ascii_uppercase if char not in key and char != "J"]
    if "J" in square: square.remove("J")
    
    pt = ["I" if char == "J" else char for char in pt]
    final = ""
    for it, char in enumerate(pt):
        if it+1 == len(pt):
            break

        if char == pt[it+1]:
            pt.insert(it+1, "X")
        
    for it in range(0, len(pt)-1, 2):
        char1 = pt[it]
        char2 = pt[it+1]

        pos1 = [square.index(char1) % 5, square.index(char1) // 5]
        pos2 = [square.index(char2) % 5, square.index(char2) // 5]

        if pos1[0] == pos2[0]:
            final += square[pos1[0]+((pos1[1]) % 5)*5] + square[pos2[0]+((pos2[1]+1) % 5)*5]
        elif pos1[1] == pos2[1]:
            final += square[(pos1[0]+1)%5 + pos1[1]*5] + square[(pos2[0]+1)%5 + pos2[1]*5]

        else:
            final += square[pos2[0] + pos1[1] * 5] + square[pos1[0] + pos2[1] *5]

    return final

        
