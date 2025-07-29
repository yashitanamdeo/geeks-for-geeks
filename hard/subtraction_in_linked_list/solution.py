# Problem Statement: https://www.geeksforgeeks.org/problems/subtraction-in-linked-list/1

#User function Template for python3

class Solution:
    def subLinkedList(self, l1, l2): 
        node = l1
        n=""
        while(node!=None):
            n+=str(node.data)
            node = node.next
        m=""
        node=l2
        while(node!=None):
            m+=str(node.data)
            node = node.next
        b = int(m)
        a = int(n)
        n = str(b-a)
        if b<a:
            n=str(a-b)
        node = Node(int(n[0]))
        head=node
        for i in range(1, len(n)):
            temp = Node(int(n[i]))
            head.next = temp
            head=temp
            
        return node



#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end='')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        ob = Solution()
        res = ob.subLinkedList(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends