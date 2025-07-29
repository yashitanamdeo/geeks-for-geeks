# Problem Statement: https://practice.geeksforgeeks.org/problems/bae68b4d6a2a77fb6bd459cf7447240919ebfbf5/1


from typing import Optional

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

You can also use the following for printing the link list.
printList(node)
"""


class Solution:
    def reverse(self, head: Optional['Node'], k: int) -> Optional['Node']:
        leng = 0
        a = head
        while a:
            leng += 1
            a = a.next
        dummy = Node(-1)
        b = dummy
        for i in range(k):
            dummy.next = head
            head = head.next
            dummy = dummy.next
        dummy.next = None

        curr, prev = b.next, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        b.next = prev

        dummy1 = Node(-1)
        c = dummy1
        for i in range(leng-k):
            dummy1.next = head
            head = head.next
            dummy1 = dummy1.next
        dummy1.next = None

        curr1, prev1 = c.next, None
        while curr1:
            temp1 = curr1.next
            curr1.next = prev1
            prev1 = curr1
            curr1 = temp1
        c.next = prev1

        dummy = Node(-1)
        res = dummy
        while prev:
            dummy.next = prev
            prev = prev.next
            dummy = dummy.next

        while prev1:
            dummy.next = prev1
            prev1 = prev1.next
            dummy = dummy.next

        return res.next


#{
 # Driver Code Starts

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while (node != None):
        print(node.data, end=" ")
        node = node.next
    print()


def inputList():
    n = int(input())  # lenght of link list
    # all data of linked list in a line
    data = [int(i) for i in input().strip().split()]
    head = Node(data[0])
    tail = head
    for i in range(1, n):
        tail.next = Node(data[i])
        tail = tail.next
    return head


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        head = inputList()

        k = int(input())

        obj = Solution()
        res = obj.reverse(head, k)

        printList(res)


# } Driver Code Ends
