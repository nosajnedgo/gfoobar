# Challenge: http://pastebin.com/izbThYPH

def answer(L, k):
    """Return max sum of sequence in L no longer than k."""
    n, max = len(L), 0
    for i in range(n):
        if L[i] <= 0:
            continue
        sum = 0
        for j in range(i, min(i+k,n)):
            sum += L[j]
            if sum > max:
                max = sum
    return max
