import string

def encrypt_bifid(pt, key):
    seen = set()
    square = [char for char in key if not (char in seen or seen.add(char))] + [char for char in string.ascii_uppercase if char not in key and char != "J"]
    if "J" in square: square.remove("J")
    pt = ["I" if char == "J" else char for char in pt]
    positions = [[square.index(char) // 5, square.index(char) % 5] for char in pt]
    new_positions = list(map(lambda x: x[0], positions)) + list(map(lambda x: x[1], positions))
    pairs = list(zip(new_positions[::2], new_positions[1::2]))
    return list(map(lambda x: square[x[0]*5 + x[1]], pairs))

