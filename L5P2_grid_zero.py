# Challenge: http://pastebin.com/jiCSPpgj

import math

class GridZero:
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)
        self.target = self._matrixToBin(matrix)
        self.masks = self._calcMaskList(self.n)
        
    def minTouches(self):
        """Return the minimum touches required to solve (-1 for DNE)"""
        if self.n % 2 == 0:
            solution = self._doTouches(0, self.target)
            return self._countBits(solution)
        if not self._parityCheck(self.n):
            return -1
        return self._oddMinTouches()

    def _oddMinTouches(self):
        """Test all possible solutions to n+1 to find minimum odd."""
        minimum = self.n**2
        if self.n % 2 == 1:
            self._extendToEven(self.matrix)        
        base = self._doTouches(0, self.target)
        # Try all bottom row possiblities with matching parity
        for i in xrange(2**(self.n - 1)):
            if self._countBits(i) % 2 != self.parity: continue
            solution = self._doTouches(base, i << 1)
            minimum = min(self._calcOddMin(solution), minimum)
        return minimum
        
    def _calcOddMin(self, solution):
        """Return the min touches for solution for an optimal right column"""
        row = int("0" + "1"*(self.n - 1) + "0", 2)
        counts = []
        for i in xrange(1, self.n):
            counts.append(self._countBits(solution & (row << i*self.n)))
        counts.sort(reverse=True)
        i, threshold = 0, self.n / 2
        while i < len(counts) and counts[i] >= threshold:
            counts[i] = self.n - 1 - counts[i]
            i += 1
        if i % 2 != self.parity:
            if i >= len(counts) - 1: i = len(counts) - 1
            if counts[i-1] > counts[i]: i -= 1
            counts[i] = self.n - 1 - counts[i]
        return sum(counts)

    def _extendToEven(self, matrix):
        """Transform current matrix to n+1 (even) matrix by adding zeros"""
        map(lambda x: x.append(0), matrix)
        matrix.append([0]*(self.n+1))
        self.__init__(matrix)
                
    def _doTouches(self, matrix, ops):
        """Apply the corresponding toggle mask for each 1 in the ops binary"""
        n2 = self.n**2
        while ops:
            i = ops & -ops
            matrix ^= self.masks[(n2-1) - int(round(math.log(i,2), 0))]
            ops -= i
        return matrix

    def _parityCheck(self, n):
        """Return whether any row or column has different even/odd parity"""
        row, col = int("0" + "1"*n, 2), int("0" + ("0"*(n-1) + "1")*n, 2)
        parity = set()
        for i in xrange(n):
            parity.add(self._countBits(self.target & row << i*n) % 2)
            parity.add(self._countBits(self.target & col << i) % 2)
        if len(parity) != 1:
            return False
        self.parity = parity.pop()
        return True

    def _calcMaskList(self, n):
        """Create a list of binary masks for each possible toggle operation"""
        row = int("0" + "1"*n + "0"*(n*n - n), 2)
        col = int("0" + ("1"+"0"*(n - 1))*n, 2)
        return [row >> (i/n)*n | col >> i%n for i in xrange(n*n)]
    
    def _matrixToBin(self, matrix):
        """Return a binary equivalent int representing the given matrix"""
        return int("0"+''.join([str(c) for r in matrix for c in r]), 2)

    def _countBits(self, num):
        """Return the count of 1's in the binary equivalent of num"""
        return bin(num).count('1')


def answer(matrix):
    gz = GridZero(matrix)
    return gz.minTouches()
