# Problem Statement: https://practice.geeksforgeeks.org/problems/reorder-list/1

#User function Template for python3

#User function Template for python3

# Node Class
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None


#Back-end complete function Template for Python 3
class Solution:

    def reorderList(self, head):
        """
    
        1. find the middle.
    
        2. reverse the second half
    
        3. merge both
    
        """

        if not head.next:

            return head

        # 1. find the middle.

        slow = head

        fast = head

        while fast.next and fast.next.next:

            slow = slow.next

            fast = fast.next.next

        head2 = slow.next

        slow.next = None

        # 2. reverse the second list

        pre = head2

        nxt = pre.next

        pre.next = None

        while nxt:

            post = nxt.next

            nxt.next = pre

            pre = nxt

            nxt = post

        head2 = pre

        #3. Merge both the list

        output = node(0)

        ptr = output

        while head and head2:

            ptr.next = head

            head = head.next

            ptr = ptr.next

            ptr.next = head2

            head2 = head2.next

            ptr = ptr.next

            ptr.next = None

        if head:

            ptr.next = head

            ptr = ptr.next

            ptr.next = None

        return output.next


#{
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = new_node

    def createList(self, arr, n):
        for i in range(n):
            self.insert(arr[i])
        return self.head

    def printList(self, head):
        tmp = head
        while tmp is not None:
            print(tmp.data, end=" ")
            tmp = tmp.next
        print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        head = lis.createList(arr, n)
        ob = Solution()
        ob.reorderList(head)

        lis.printList(head)

# } Driver Code Ends
