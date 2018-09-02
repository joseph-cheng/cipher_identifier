import string
import stats_utils
import itertools
import math
import stats_data
import time

def get_ic(ct):
    length = len(ct)
    ic = 0
    for char in string.ascii_uppercase:
        ic += (ct.count(char)*(ct.count(char)-1))/(length*(length-1))
    return ic

def max_p_ic(ct):
    #t1 = time.time()

    max_ic = 0
    for period in range(1,16):
        if period >= len(ct):
            break
        x = get_ic(cipher_utils.split_by_period(ct, period))
        if x > max_ic:
            max_ic = x
    #print("Max pic", time.time()-t1)

    return max_ic

def kappa(ct1, ct2):
    
    zipped = list(zip(ct1, ct2))
    count = 0
    for comparison in zipped:
        if comparison[0] == comparison[1]:
            count += 1

    return count/min(len(ct1), len(ct2))

def max_kappa(ct):
    #t1 = time.time()

    max_k = 0
    for period in range(1, 16):
        if period >= len(ct):
            break
        x = kappa(ct, ct[period:])
        if x > max_k:
            max_k = x
    
   # print("Max Kappa",time.time()-t1)

    return max_k

def digraphic_ic(ct):
    #t1 = time.time()

    ic = 0
    length = len(ct)
    for pair in list(map(lambda x: "".join(x), list(itertools.product(string.ascii_uppercase, string.ascii_uppercase)))):
        ic += (ct.count(pair)*(ct.count(pair)-1))/((length-1)*(length-2))
   # print("digraphic ic", time.time()-t1)

    return ic

def even_d_ic(ct):
    #t1 = time.time()

    pairs = [ct[i:i+2] for i in range(0, len(ct), 2)]
    if len(pairs[-1]) == 1:
        pairs.pop()
    length = len(pairs)
    ic = 0
    for pair in list(map(lambda x: "".join(x), list(itertools.product(string.ascii_uppercase, string.ascii_uppercase)))):
        ic += (pairs.count(pair)*(pairs.count(pair)-1))/((length-1)*(length-2))
    #print("even dic", time.time()-t1)

    return ic

def long_repeat(ct):
    #t1 = time.time()

    length = len(ct)
    r3 = 0
    for i in range(length-3):
        for j in range(i+1, length):
            n = 0
            for k in range(length-j):
                if ct[i+k] != ct[j+k]:
                    break
                n += 1
            if n == 3:
                r3 += 1
    #print("long repeat", time.time()-t1)

    return math.sqrt(r3)/length

def rod(ct):
    #t1 = time.time()

    length = len(ct)
    sum_odd = 0
    sum_all = 0
    for i in range(length-1):
        for j in range(i+1, length):
            n = 0
            for k in range(length-j):
                if ct[i+k] != ct[j+k]:
                    break
                n += 1
            if n > 1:
                sum_all += 1
                if (j-i) % 2 == 1:
                    sum_odd += 1
    #print("rod", time.time()-t1)

    return sum_odd/sum_all

def log_digraph(ct):
    #t1 = time.time()

    length = len(ct) - 1
    score = 0
    for it in range(0, length):
        pair = ct[it:it+2]
        index = (ord(pair[0]) - 65) * 26 + ord(pair[1]) - 65
        
        score += stats_data.log_digraph_scores[index]
    #print("log digraph", time.time()-t1)

    return (score/length)/9

def sdd(ct):
    #t1 = time.time()

    length = len(ct) - 1
    score = 0
    for it in range(0, length):
        pair = ct[it:it+2]
        index = (ord(pair[0]) - 65) * 26 + ord(pair[1]) - 65
        
        score += stats_data.single_letter_digraph_discrepancy[index]
    #print("sdd", time.time()-t1)

    return (score/length)/9

def normor(ct):
    #t1 = time.time()

    frequencies = []
    for char in string.ascii_uppercase:
        frequencies.append([char, ct.count(char)])
    frequencies = sorted(frequencies, key=lambda x: x[1], reverse=True)
    frequencies = list(map(lambda x:x[0], frequencies))

    score = 0
    english_freqs = "ETAOINSRHLDUCMGFYPWBVKXJZQ"
    for it, char in enumerate(frequencies):
        score += abs(it-english_freqs.index(char))
    #print("nomor", time.time()-t1)

    return score/350

def div_2(ct):
    return not(len(ct)%2)

def div_3(ct):
    return not(len(ct)%3)

def has_j(ct):
    return "J" in ct

stats_funcs = [get_ic, max_p_ic, max_kappa, digraphic_ic, even_d_ic, log_digraph, sdd, normor, div_2, div_3, has_j]
