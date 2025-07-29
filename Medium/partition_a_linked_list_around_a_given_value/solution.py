# Problem Statement: https://practice.geeksforgeeks.org/problems/partition-a-linked-list-around-a-given-value/1

#User function Template for python3

"""

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""
class Solution:
    def partition(self, head, x):
        a = Node(-1)
        b = Node(-1)
        c = Node(-1)
        ans1 = a
        ans2 = b
        ans3 = c
        while head:
            if head.data<x:
                a.next = Node(head.data)
                a = a.next
            elif head.data >x:
                c.next = Node(head.data)
                c = c.next
            else:
                b.next = Node(head.data)
                b = b.next
            head = head.next
        b.next = ans3.next
        a.next = ans2.next
        return ans1.next

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        ob=Solution()
        new_head = ob.partition(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1




# } Driver Code Ends