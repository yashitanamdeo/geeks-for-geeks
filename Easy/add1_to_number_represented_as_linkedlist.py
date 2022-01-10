# Problem Statement: https://practice.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1#

#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        temp = head
        num = 0
        numberOfDigits = 0
       
       #Extracting the digits, forming number, counting the number of digits 
        while temp != None:
            num = num * 10 + temp.data
            numberOfDigits = numberOfDigits + 1
            temp = temp.next
           
        temp = head

      #Adding 1 to the number
        num = num + 1  
        divisor = 10 ** (numberOfDigits-1)

      #Extracting the digits from number and storing in linked list
        while divisor > 0 and temp != None:
            digit = num // divisor
            temp.data = digit
            temp = temp.next
            num = num % divisor
            divisor = divisor // 10
       
        return head
#{ 
#  Driver Code Starts
#Initial Template for Python 3

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
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

def PrintList(head):
    while head:
        print(head.data,end='')
        head = head.next

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        num = input()
        ll = LinkedList() # create a new linked list 'll1'.
        for digit in num:
            ll.insert(int(digit))  # add to the end of the list
        
        resHead = Solution().addOne(ll.head)
        PrintList(resHead)
        print()


# } Driver Code Ends