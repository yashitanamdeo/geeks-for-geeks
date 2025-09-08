# Problem Statement: https://www.geeksforgeeks.org/problems/sort-a-linked-list/1

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def mergeSort(self, head):
        initAns=[]
        new=head
        while new:
            initAns.append(new.data)
            new=new.next
        initAns.sort()    
        current=head
        for i in initAns:
            current.data=i
            current=current.next
        return head