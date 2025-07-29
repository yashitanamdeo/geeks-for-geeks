# Problem Statement: https://practice.geeksforgeeks.org/problems/de6f6a196aecdfb3e4939ba7729809a5a4bdfe90/1

#User function Template for python3

class Solution:
    def findAnagrams(self, head, s):
        N = len(s)
        TAR = [0]*26
        for c in s:
            TAR[ord(c)-97] += 1
        ans, h, t, F = [], head, head, None
        while t:
            if F is None:
                F = [0]*26
                for _ in range(N):
                    if t is None:
                        break
                    F[ord(t.data)-97] += 1
                    t = t.next
            else:
                F[ord(h.data)-97] -= 1
                F[ord(t.data)-97] += 1
                h, t = h.next, t.next

            if F == TAR:
                ans.append(h)
                while h.next != t:
                    h = h.next
                h.next = None
                h = t
                F = None

        return ans


#{
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self):
        self.data = None
        self.next = None

# Linked List Class


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head == None:
            self.head = Node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = Node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next


def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')


# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(str, input().strip().split()))
        for i in values:
            list1.insert(i)
        s = input()
        res = Solution().findAnagrams(list1.head, s)
        for i in range(len(res)):
            printlist(res[i])
        if len(res) == 0:
            print(-1)

# } Driver Code Ends
