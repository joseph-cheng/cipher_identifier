def encrypt_transposition(pt, key):
    ptLen = len(pt)
    keyLen = len(key)
    if ptLen / keyLen != ptLen // keyLen:
        pt = pt + ["X"] * (keyLen - ptLen % keyLen)
    ptLen = len(pt)
    columns = [[key[x], [pt[y+x] for y in range(0, ptLen-x, keyLen)]] for x in range(keyLen)]
    rearranged = sorted(columns, key=lambda x:x[0])
    return "".join(["".join([column[1][x] for column in rearranged]) for x in range(int(ptLen/keyLen))])
