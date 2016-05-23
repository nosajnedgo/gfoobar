# Challenge: http://pastebin.com/H3cp5pqk

from fractions import gcd

class Carrotland():

    def __init__(self, vertices):
        vertices.sort()
        self.vertices = vertices

    def count(self):
        """Return the count of integers found inside the triangle"""
        V, X, Y = self.vertices, 0, 1
        count = self._calcSquare(V, 1)
        for a, b in [(0,1), (1,2), (0,2)]:
            count -= self._calcRightTriangle(V[a], V[b])
        if (V[0][Y] < V[1][Y] < V[2][Y]) or (V[0][Y] > V[1][Y] > V[2][Y]):
            hiLeft = self._calcSquare([ V[1], [ V[0][X], V[2][Y] ] ], 0)
            loRite = self._calcSquare([ V[1], [ V[2][X], V[0][Y] ] ], 0)
            count -= min(hiLeft, loRite)
        return count

    def _calcSquare(self, vertices, add):
        """Return count of integers in a square circumscribing the list range"""
        xList, yList = zip(*vertices)
        x = abs(max(xList) - min(xList)) + add
        y = abs(max(yList) - min(yList)) + add
        return x * y

    def _calcRightTriangle(self, v1, v2):
        """Calc integers found within a right triangle between two vertices """
        x, y = abs(v1[0] - v2[0]), abs(v1[1] - v2[1])
        return ( (x + 1) * (y + 1) + gcd(x,y) ) / 2
        

def answer(vertices):
    carrots = Carrotland(vertices)
    return carrots.count()