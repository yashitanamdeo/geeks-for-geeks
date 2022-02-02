# Problem Statement: https://practice.geeksforgeeks.org/problems/find-position-of-set-bit3706/1

#User function Template for python3

class Solution:
    def findPosition(self,N):
        if N ==0:
            return -1
        binary = list('{0:b}'.format(int(N)))
        if binary.count('1')>1:
            return -1
        elif binary.count('1')==1:
            list1 = binary[::-1]
            for t in list1:
                if t =='1':
                    return list1.index(t)+1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.findPosition(N))
# } Driver Code Ends