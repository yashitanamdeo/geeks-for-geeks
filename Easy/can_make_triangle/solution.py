# Problem Statement: https://practice.geeksforgeeks.org/problems/51b7f8fb8b33d657a857f230361b7dad6565ce62/1

#User function Template for python3
class Solution:
    def canMakeTriangle(self, A, N): 
        output = []
        for i in range(N-2) :
            a = A[i]
            b = A[i+1]
            c = A[i+2]
            if(a+b > c and a+c > b and b+c > a) :
                output.append(1)
            else :
                output.append(0)
        return output

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.canMakeTriangle(A, N)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends