# Problem Statement: https://practice.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1

#User function Template for python3
'''
	Your task is to merge the given k sorted
	linked lists into one list and return
	the the new formed linked list class.

	Function Arguments:
	    arr is a list containing the n linkedlist head pointers
	    n is an integer value
    
    node class:
    
class Node:
    def __init__(self,x):
        self.data = x
        self.nxt = None
'''
class Solution:
    #Function to merge K sorted linked list.
    def mergeKLists(self,arr,K):
       # code here
       # return head of merged list
        l=[]
        for i in arr:
            temp = i
            while temp:
                l.append(temp.data)
                temp = temp.next
        l.sort()
        head = Node(l[0])
        str = head
        for i in range(1,len(l)):
            node = Node(l[i])
            str.next=node
            str = node
        return head
    

class Solution2:
    def mergeKLists(self, arr):
        import heapq
        hp=[(nd.data,ix,) for ix,nd in enumerate(arr)]
        heapq.heapify(hp)
        dum=Node(-1)
        cur=dum
        while hp:
            _,ix=heapq.heappop(hp)
            cur.next=arr[ix]
            cur=cur.next
            arr[ix]=arr[ix].next
            if arr[ix]:
                heapq.heappush(hp,(arr[ix].data,ix,))
        return dum.next

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,x):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.next=Node(x)
            self.tail=self.tail.next
    
def printList(head):
    walk = head
    while walk:
        print(walk.data, end=' ')
        walk=walk.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        line=[int(x) for x in input().strip().split()]
        
        heads=[]
        index=0
        
        for i in range(n):
            size=line[index]
            index+=1
            
            newList = LinkedList()
            
            for _ in range(size):
                newList.add(line[index])
                index+=1
            
            heads.append(newList.head)
        
        merged_list = Solution().mergeKLists(heads,n)
        printList(merged_list)

# } Driver Code Ends