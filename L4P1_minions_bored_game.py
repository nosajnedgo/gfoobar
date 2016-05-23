# Challenge: http://pastebin.com/q6FeBZ5C

class MinionBored():

    def __init__(self, t, n):
        self.memoize = {}
        self.t = t
        self.n = n
    
    def calc(self, t, n):
        if n == self.n+2:
            return 0
        elif n == 2:
            return t;
        elif t < n-1:
            return 0
        else:
            key = (t,n)
            val = self.memoize.get(key)
            if val is None:
                val = self.calc(t-1,n-1) + self.calc(t-1,n) + self.calc(t-1,n+1)
                val = self.memoize[key] = value % 123454321
            return val

    def answer(self):
        return self.calc(self.t, self.n)

def answer(t, n):
    game = MinionBored(t, n)
    return game.answer()
