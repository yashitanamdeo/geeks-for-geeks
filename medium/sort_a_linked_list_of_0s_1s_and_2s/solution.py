# Problem Statement: https://practice.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1

# User function Template for python3
'''
	Your task is to segregate the list of 
	0s,1s and 2s.
	
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
import sys
import io
import atexit


class Solution:
    # Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        c = [0]*3
        curr = head
        while curr:
            c[curr.data] += 1
            curr = curr.next
        i = 0
        curr = head
        while curr:
            if c[i]:
                curr.data = i
                c[i] -= 1
                curr = curr.next
            else:
                i += 1
        return head


class Solution2:
    def segregate(self, head):
        zero,one,two=Node(-1),Node(-1),Node(-1)
        zh,oh,th=zero,one,two
        curr=head
        while curr:
            if curr.data==0:
                zero.next=curr
                zero=zero.next
            elif curr.data==1:
                one.next=curr
                one=one.next
            else:
                two.next=curr
                two=two.next
            curr=curr.next
        zero.next,one.next,two.next=None,None,None
        head=Node(-1)
        tail=head
        if zh.next:
            tail.next=zh.next
            tail=zero
        if oh.next:
            tail.next=oh.next
            tail=one
        if th.next:
            tail.next=th.next
            tail=two
        return head.next

# {
 # Driver Code Starts
# Initial Template for Python 3
# Contributed by : Nagendra Jha
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
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
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

# prints the elements of linked list starting with head


def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next
    print()


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        printList(Solution().segregate(a.head))
# } Driver Code Ends
