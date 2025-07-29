# Problem Statement: https://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1

"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""


class Solution:
    def reverse(self, head, k):
        # convert to list
        res_ls = []
        curr = head
        while curr is not None:
            res_ls.append(curr.data)
            curr = curr.next

        # process and order it as per the question
        n = len(res_ls)
        for i in range(0, n, k):
            start = i
            end = min(i + k - 1, n - 1)
            while start < end:
                res_ls[start], res_ls[end] = res_ls[end], res_ls[start]
                start += 1
                end -= 1
        # push back to linkedlist and return the head
        l = LinkedList()
        for i in reversed(res_ls):
            l.push(i)

        return l.head


# {
 # Driver Code Starts
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
        ob = Solution()
        new_head = ob.reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1


# } Driver Code Ends
