# Problem Statement: https://www.geeksforgeeks.org/problems/arrange-consonants-and-vowels/1

#User function Template for python3

"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    vowels={"a","e","i","o","u"}

    def arrangeCV(self, head):
        curr=head
        vHead,vTail=None,None
        cHead,cTail=None,None
        while curr:
            if curr.data in self.vowels:
                if vHead:
                    vTail.next=curr
                else:
                    vHead=curr
                vTail=curr
            else:
                if cHead:
                    cTail.next=curr
                else:
                    cHead=curr
                cTail=curr
            curr=curr.next
        if cTail:
            cTail.next=None
        if vTail:
            vTail.next=cHead
        return vHead if vHead else cHead


#{ 
 # Driver Code Starts
# Node Class
class Node:

    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp = tmp.next
    print()


if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [str(x) for x in input().split()]

        lis = Linked_List()
        for i in arr:
            lis.insert(i)

        newHead = Solution().arrangeCV(lis.head)
        printList(newHead)

# } Driver Code Ends