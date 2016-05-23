# Challenge: http://pastebin.com/MvLSdU2A

from math import factorial

def nChooseK(n, k):
    """n choose k binomial coefficient"""
    return factorial(n) // factorial(k) // factorial(n-k)

class BSTNode():
    """A single Node in the Binary Search Tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BunnyBST():
    def __init__(self, seq):
        self.root = BSTNode(seq[0])
        for val in seq[1:]:
            self._insert(self.root, val)

    def countSequences(self):
        """Return the number of sequences that result in the same tree"""
        return self._perms(self.root)
        
    def _insert(self, node, value):
        """Insert a new BSTNode into the BST"""
        if node.value < value:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert(node.right, value)

    def _perms(self, n):
        """Recursively calc the number of permutations for each sub tree"""
        if not n: return 1
        leftCount, rightCount = self._count(n.left), self._count(n.right)
        myPerms = nChooseK(leftCount + rightCount, leftCount)
        return myPerms * self._perms(n.left) * self._perms(n.right)
            
    def _count(self, node):
        """Return the sub tree size including self"""
        if not node: return 0
        return self._count(node.left) + self._count(node.right) + 1
    

def answer(seq):
    tree = BunnyBST(seq)
    return tree.countSequences()