# Problem Statement: https://www.geeksforgeeks.org/problems/merge-2-sorted-linked-list-in-reverse-order/1

#User function Template for python3

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''

class Solution:
    def mergeResult(self, h1, h2):
        #return head of merged list
        h=None
        while(h1 and h2):
            if(h1.data<h2.data):
                if h:
                    k=Node(h1.data)
                    k.next=h
                    h=k
                else:
                    h=Node(h1.data)
                h1=h1.next
            else:
                if h:
                    k=Node(h2.data)
                    k.next=h
                    h=k
                else:
                    h=Node(h2.data)
                h2=h2.next
        while(h1):
            if h:
                k=Node(h1.data)
                k.next=h
                h=k
            else:
                h=Node(h1.data)
            h1=h1.next
        while(h2):
            if h:
                k=Node(h2.data)
                k.next=h
                h=k
            else:
                h=Node(h2.data)
            h2=h2.next
        return h


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

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
        
        n1,n2=[int(x) for x in input().split()]
        
        arr1=[int(x) for x in input().split()]
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
            
        arr2=[int(x) for x in input().split()]
        ll2=Llist()
        tail=None
        for nodeData in arr2:
            tail=ll2.insert(nodeData,tail)
        
        
        ob = Solution()
        resHead=ob.mergeResult(ll1.head,ll2.head)
        printList(resHead)
        print()
        
    
    
# } Driver Code Ends