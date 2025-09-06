# Problem Statement: https://www.geeksforgeeks.org/problems/find-length-of-loop/1

'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        curr=head
        l=0
        c=0
        while curr:
            curr.data=-1*(curr.data)
            l+=1
            if curr.data>0:
                break
            curr=curr.next
        curr2=head
        while curr2:
            if curr2.data>0:
                return l-c-1
            c+=1
            curr2=curr2.next
        return 0

