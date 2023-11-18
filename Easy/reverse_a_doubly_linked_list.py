# Problem Statement: https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1

# User function Template for python3

'''
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
'''


class Solution:
    def reverseDLL(self, head):

        prevnode = None
        curr = head

        while curr.next != None:
            nextnode = curr.next
            curr.next = prevnode
            curr.prev = nextnode
            prevnode = curr
            curr = nextnode

        newhead = curr
        newhead.next = newhead.prev

        return newhead


# {
 # Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data, tail):
        if not self.head:
            self.head = Node(new_data)
            return self.head
        Nnode = Node(new_data)
        Nnode.prev = tail
        tail.next = Nnode
        return Nnode

    def printList(self, node):
        while (node is not None):
            print(node.data, end=' ')
            node = node.next


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        dll = DoublyLinkedList()
        tail = None

        for e in arr:
            tail = dll.push(e, tail)

        ob = Solution()
        resHead = ob.reverseDLL(dll.head)
        dll.printList(resHead)
        print()

# } Driver Code Ends
