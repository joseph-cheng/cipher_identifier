import string

def encrypt_two_square(pt, key1, key2, horizontal):

    seen = set()
    square1 = [char for char in key1 if not (char in seen or seen.add(char))] + [char for char in string.ascii_uppercase if char not in key1 and char != "J"]
    seen = set()
    square2 = [char for char in key2 if not (char in seen or seen.add(char))] + [char for char in string.ascii_uppercase if char not in key2 and char != "J"]
    if "J" in square1: square1.remove("J")
    if "J" in square2: square2.remove("J")
    pt = ["I" if char == "J" else char for char in pt]
    final = ""
    for it in range(0, len(pt)-1, 2):
        char1 = pt[it]
        char2 = pt[it+1]

        pos1 = [square1.index(char1) % 5, square1.index(char1) // 5]
        pos2 = [square2.index(char2) % 5, square2.index(char2) // 5]
        
        if (horizontal and pos1[1] == pos2[1]) or ((not(horizontal)) and pos1[0] == pos2[0]):
            final += char1 + char2
        else:
            if horizontal:
                final += square1[pos1[0] + pos2[1]*5] + square2[pos2[0] + pos1[1]*5]
            else:
                final += square1[pos2[0] + pos1[1]*5] + square2[pos1[0] + pos2[1]*5]


    return final

