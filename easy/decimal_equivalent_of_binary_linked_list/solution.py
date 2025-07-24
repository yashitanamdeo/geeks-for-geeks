# Problem Statement: https://www.geeksforgeeks.org/problems/decimal-equivalent-of-binary-linked-list/1

# your task is to complete this function
# Function should return an integer value

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def decimalValue(self, head):
        # Define a constant for modulo operation
        MOD = 10**9 + 7
        # Initialize the result variable to store the decimal value
        decimal_value = 0

        # Traverse the binary linked list
        while head:
            # Update the result by left-shifting and adding the current binary digit
            decimal_value = (decimal_value * 2 + head.data) % MOD
            # Move to the next node in the linked list
            head = head.next

        # Return the final decimal value
        return decimal_value


#{ 
 # Driver Code Starts
# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        ob=Solution()
        print(ob.decimalValue(list1.head))
# Contributed By: Harshit Sidhwa
# } Driver Code Ends