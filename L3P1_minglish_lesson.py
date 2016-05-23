# Challenge: http://pastebin.com/k0RfRD2w

class Minglish:
    def __init__(self, words):
        self.graph = {}
        self.visited = set()
        self.revSort = ""
        self.addWords(words)

    def addWords(self, words):
        for i in range(len(words)-1):
            for char in words[i] + words[i+1]:
                if not self.graph.get(char):
                    self.graph[char] = []
            vertex, edge = self.findEdge(words[i], words[i+1])
            if vertex and edge:
                self.graph[vertex].append(edge)

    def findEdge(self, word1, word2):
        length = min(len(word1), len(word2))
        for i in range(length):
            if word1[i] != word2[i]:
                return word1[i], word2[i]
        return None, None

    def getAlphabet(self):
        self.topSort()
        return self.revSort[::-1]

    def topSort(self):
        for vertex, edge in self.graph.iteritems():
            if vertex not in self.visited:
                self.visitVertex(vertex)

    def visitVertex(self, vertex):
        if vertex not in self.visited:
            for edge in self.graph[vertex]:
                self.visitVertex(edge)
            self.visited.add(vertex)
            self.revSort += vertex

def answer(words):
    minglish = Minglish(words)    
    return minglish.getAlphabet()