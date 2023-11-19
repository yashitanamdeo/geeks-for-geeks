# Problem Statement: https://www.geeksforgeeks.org/problems/intersection-of-two-sorted-linked-lists/1

# User function Template for python3

''' structure of node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''

from collections import defaultdict


class Solution:
    def findIntersection(self, head1, head2):
        # return head
        dic = defaultdict(int)
        curr1 = head1

        while curr1:
            dic[curr1.data] += 1
            curr1 = curr1.next
        # for i in dic:
        #     print(i)

        temp = None
        newHead = None
        prevNode = None
        curr2 = head2

        while curr2:
            if curr2.data in dic:
                dic[curr2.data] -= 1
                if dic[curr2.data] == 0:
                    del dic[curr2.data]

                temp = Node(curr2.data)
                if newHead == None:
                    newHead = temp
                else:
                    prevNode.next = temp

                # change the position of prevNode
                prevNode = temp
            curr2 = curr2.next

        return newHead


# {
 # Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n1, n2 = [int(x) for x in input().split()]
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)

        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        ob = Solution()
        result = ob.findIntersection(ll1.head, ll2.head)
        printList(result)
        print()

# } Driver Code Ends
