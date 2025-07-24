# Problem Statement: https://practice.geeksforgeeks.org/problems/find-length-of-loop/1

# User function Template for python3

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''

# Function to find the length of a loop in the linked list.


def countNodesinLoop(head):
    # Your code here
    fastptr = head
    slowptr = head
    flag = 0
    # check if there is a loop
    while(fastptr != None and fastptr.next != None):
        slowptr = slowptr.next
        fastptr = fastptr.next.next
        if fastptr == slowptr:
            flag = 1
            break
    # calculate loop length
    if flag == 1:
        temp = slowptr
        count = 0
        while(temp.next != slowptr):
            count += 1
            temp = temp.next
        return count+1
    return 0

# {
#  Driver Code Starts
# Initial Template for Python 3

# Node Class


class Node:
    def __init__(self, data):   # data -> value stored in node
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

    # connects last node to node at position pos from begining.
    def loopHere(self, pos):
        if pos == 0:
            return

        walk = self.head
        for i in range(1, pos):
            walk = walk.next

        self.tail.next = walk


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())

        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))

        LL.loopHere(int(input()))

        print(countNodesinLoop(LL.head))

# } Driver Code Ends
