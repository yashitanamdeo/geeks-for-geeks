# Problem Statement: https://www.geeksforgeeks.org/problems/linked-list-that-is-sorted-alternatingly/1

#User function Template for python3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    def reverse(self, head):
        temp = None
        curr = head
        
        while curr:
            nxt = curr.next
            curr.next = temp
            temp = curr
            curr = nxt
        
        head = temp
        return head
    
    def sort(self, h1):
        if not h1 or not h1.next: return h1
        
        dleft = left = Node(0)
        dright = right = Node(0)
        
        while h1:
            left.next = h1
            left = left.next
            h1 = h1.next
            if h1:
                right.next = h1
                right = right.next
                h1 = h1.next
        left.next = None
        right.next = None
                
        left = dleft.next
        right = self.reverse(dright.next)
        
        le = left
        ri = right
        
        return self.merge(left, right)
        
    def merge(self, left, right):
        tail = dummy = Node(0)
        
        while left and right:
            if left.data<right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left:
            tail.next = left
        if right:
            tail.next = right
        return dummy.next
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1=int(input())
        arr1=[int(x) for x in input().split()]
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
        
        ob = Solution()
        resHead=ob.sort(ll1.head)
        printList(resHead)
        print()
        
    
    
# } Driver Code Ends