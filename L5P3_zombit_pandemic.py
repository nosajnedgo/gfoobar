# Challenge: http://pastebin.com/JEdZ7zSA

from math import factorial
import fractions 

nCkMemo, sGcMemo = {}, {}

def answer(n):
    counts = getCounts(n)
    num, den = sum([s * c for s, c in counts.iteritems()]), (n-1)**n
    gcd = fractions.gcd(num, den)
    return "{}/{}".format(num/gcd, den/gcd)

def getCounts(n):
    """Return a dictionary of [max group size] => [number of occurences]"""
    counts = {}
    for groups in possibleGroups(n, 2):
        maxSize, repeats = groups[-1], {}
        sub, total, dups, used = 1, 1, 1, 0
        for g in groups:
            sub *= nChooseK(n - used, g)
            total *= singleGroupCount(g)
            repeats[g] = repeats.get(g,0) + 1
            used += g
        for i, cnt in repeats.iteritems():
            dups *= factorial(cnt)
        counts[maxSize] = counts.get(maxSize,0) + sub * total / dups 
    return counts

def possibleGroups(n, start):
    """Generator for all possible resulting groups of bunnies"""
    for i in range(start, n+1):
        if n == i: yield [ i ]
        if n - i < i: continue
        for p in possibleGroups(n-i, i):
            yield [ i ] + p

def nChooseK(n, k):
    """Memoized n choose k binomial coefficient"""
    if (n,k) not in nCkMemo:
        nCkMemo[(n,k)] = factorial(n) // factorial(k) // factorial(n-k)
    return nCkMemo[(n,k)]

def singleGroupCount(n):
    """Memoized calc of total ways to form one group of size n"""
    if n not in sGcMemo:
        totals = [nChooseK(n,k) * (n-k)**(n-k) * (k ** k) for k in xrange(1, n)]
        sGcMemo[n] = sum(totals) / n
    return sGcMemo[n]
