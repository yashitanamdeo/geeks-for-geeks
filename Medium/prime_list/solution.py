# Problem Statement: https://practice.geeksforgeeks.org/problems/6cb0782855c0f11445b8d70e220f888e6ea8e22a/1

from typing import Optional
import math

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
    def isPrime(self, num):
        if num == 2:
            return True
        else:
            k = 2
            while k <= math.sqrt(num):
                if num % k == 0:
                    return False
                k += 1
            return True

    def primeList(self, head: Optional['Node']) -> Optional['Node']:
        # code here
        temp = head
        test1, test2 = 0, 0
        while temp != None:
            data = temp.data
            if data == 1:
                temp.data = 2
                continue
            test1 = test2 = data
            while self.isPrime(test2) == False:
                test2 += 1
            while self.isPrime(test1) == False:
                test1 -= 1
            if (data-test1) <= (test2-data):
                data = test1
            else:
                data = test2
            temp.data = data
            temp = temp.next
        return head


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

        obj = Solution()
        res = obj.primeList(head)

        printList(res)


# } Driver Code Ends
