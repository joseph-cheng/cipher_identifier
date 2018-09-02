import numpy as np
def encrypt_hill_2(pt, key):
    final = ""
    
    if len(pt) % 2:
        pt += "Z"
    keyMat = np.array([[ord(key[0])-65, ord(key[1])-65],
                       [ord(key[2])-65, ord(key[3])-65]])
    
    for i in range(0, len(pt)-1, 2):
        pair = np.array([[ord(pt[i])-65],[ord(pt[i+1])-65]])
        final += matrix_to_letters((np.matmul(keyMat, pair))%26)
    return final
    

def encrypt_hill_3(pt, key):
    final = ""

    if len(pt) % 3:
            pt += "Z" * (3 - len(pt) % 3)

    keyMat = keyMat = np.array([[ord(key[0])-65, ord(key[1])-65, ord(key[2])-65],
                                [ord(key[3])-65, ord(key[4])-65, ord(key[5])-65],
                                [ord(key[6])-65, ord(key[7])-65, ord(key[8])-65]])
    for i in range(0, len(pt)-2, 23):
        pair = np.array([[ord(pt[i])-65],[ord(pt[i+1])-65],[ord(pt[i+2])-65]])
        final += matrix_to_letters((np.matmul(keyMat, pair))%26)
    return final


def matrix_to_letters(m):
    return "".join([chr(x+65) for x in m])


    
