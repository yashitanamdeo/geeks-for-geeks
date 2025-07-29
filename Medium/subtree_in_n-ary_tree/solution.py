# Problem Statement: https://practice.geeksforgeeks.org/problems/079dee7e7db7a784ed73f604e3cf1712432edf79/1

#User function Template for python3

'''
class Node:
	def __init__(self, key, children=None):
		self.key = key
		self.children = children or []
	
	def __str__(self):
		return str(self.key)
'''

from collections import deque
from collections import defaultdict


class Solution:
    def cst(self, root, sp):
        s = str(root.key)
        for y in root.children:
            s += self.cst(y, sp)
        sp[s] = sp.get(s, 0)+1
        return s

    def duplicateSubtreeNaryTree(self, root):
        sp = {}
        self.cst(root, sp)
        c = 0
        for x in sp:
            if sp[x] > 1:
                c += 1
        return c


#{
 # Driver Code Starts
#Initial Template for Python 3


class NodeNotFoundException(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)


class Node:
	def __init__(self, key, children=None):
		self.key = key
		self.children = children or []

	def __str__(self):
		return str(self.key)


class N_ary_Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def find_node(self, node, key):
        if node == None or node.key == key:
            return node
        for child in node.children:
            return_node = self.find_node(child, key)
            if return_node:
                return return_node
        return None

    def add(self, new_key, parent_key=None):
        new_node = Node(new_key)
        if parent_key == None:
            self.root = new_node
            self.size = 1
        else:
            parent_key.children.append(new_node)
            self.size += 1
        return new_node


if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):

        N = [el for el in input().split()]
        '''
        N-ary Tree Building
        '''

        tree = N_ary_Tree()
        curr = 0
        for i in range(len(N)):
            if i == 0:
                q = deque()
                curr = tree.add(int(N[0]))
            elif N[i] == " " or N == "\n":
                continue
            elif q and N[i] == "N":
                curr = q.popleft()
            elif N[i] != "N":
                q.append(tree.add(int(N[i]), curr))

        res = Solution().duplicateSubtreeNaryTree(tree.root)
        print(res)
# } Driver Code Ends
