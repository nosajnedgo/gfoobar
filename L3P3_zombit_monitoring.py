# Challenge: http://pastebin.com/mqrwiXEv

def reduceList(X):
    length = len(X);
    for A in range(0, length):
        B = A + 1;
        while (B < length):
            if X[B][0] > X[A][1] or X[B][1] < X[A][0]:
                B += 1;
                continue
            if X[B][0] >= X[A][0] and X[B][1] <= X[A][1]:
                X.pop(B)
                return
            if X[B][0] <= X[A][0] and X[B][1] >= X[A][1]:
                X.pop(A)
                return
            if X[B][0] <= X[A][0]:
                X[A][0] = X[B][0]
                X.pop(B)
                return
            if X[B][1] >= X[A][1]:
                X[A][1] = X[B][1]
                X.pop(B)
                return            

def addIntervals(intervals):
    return sum(map(lambda x: x[1] - x[0], intervals))

def answer(intervals):
    while True:
        oldLen = len(intervals)
        reduceList(intervals)
        newLen = len(intervals)
        if (newLen == oldLen):
            break
    return addIntervals(intervals);