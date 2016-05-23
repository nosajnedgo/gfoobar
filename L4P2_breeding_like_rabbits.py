# Challenge: http://pastebin.com/d39N4KnD

class ZombitFib():
    """Calculates Zombit Fibonachi-like numbers"""    
    cache = { 0:1, 1:1, 2:2 }

    def findMaxN(self, target):
        """Search through odds first, then evens."""
        lo, hi = 0, target
        result = self.search(lo, hi, False, target)
        if result is None:
            result = self.search(lo, hi, True, target)
        return result

    def search(self, lo, hi, even, target):
        """Odd/Even binary search for N that yields target."""
        while lo < hi:
            mid = (lo + hi) // 2
            if even and mid % 2 == 1: mid = mid - 1
            if not even and mid % 2 == 0: mid = mid - 1
            test = self.R(mid)
            if test == target: return mid
            elif test < target: lo = mid + 2
            else: hi = mid
        return None

    def R(self, N):
        """Recursively calculate R for given N"""
        if N not in self.cache:
            if N % 2 == 1:
                n = (N-1)/2
                self.cache[N] = self.R(n-1) + self.R(n) + 1
            else:
                n = N/2
                self.cache[N] = self.R(n) + self.R(n+1) + n 
        return self.cache[N]


def answer(str_S):
    S = int(str_S, 10)
    zFib = ZombitFib()
    result = zFib.findMaxN(S)
    return str(result)
