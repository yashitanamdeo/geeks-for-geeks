# Problem Statement: https://practice.geeksforgeeks.org/problems/7488b7721e8aa5e5fc37d56af8b9c89e329c796f/1

#User function Template for python3

class Solution():
    def modulo(self, s, m):
        return int(s, 2)%m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s,m = input().split()
        m = int(m)
        print(Solution().modulo(s, m))

# } Driver Code Ends