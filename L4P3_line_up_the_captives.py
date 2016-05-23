# Challenge: http://pastebin.com/40Nu4AXB

def base(x, y, n):
    """Iterative solution to (X=1, Y=x+y-1, N=n)"""
    curRow = [i for i in range(0, n)]
    for N in range(2,n):
        curRow[N] = curRow[N-1]*(N-1)
    for _ in range(3, x+y):
        lastRow = curRow[:]
        for N in range(1, n):
            curRow[N] = curRow[N-1]*(N-1) + lastRow[N-1]
    return curRow[n-1]

def multiple(x, y):
    """Iterate to find the multiple for a given x, y pair"""
    curRow = [1] * x
    for _ in range(1,y):
        for N in range(1,x):
            curRow[N] = curRow[N-1] + curRow[N]
    return curRow[x-1]

def answer(x, y, n):
    return base(x, y, n) * multiple(x, y)
