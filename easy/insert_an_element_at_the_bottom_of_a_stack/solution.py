# Problem Statement: https://www.geeksforgeeks.org/problems/insert-an-element-at-the-bottom-of-a-stack/1

#User function Template for python3
class Solution:
    def insertAtBottom(self,st,x):
        # code here
        st.insert(0, x)
        return st

#{ 
 # Driver Code Starts

if __name__ == "__main__":
    for _ in range(int(input())):
        n,x = map(int,input().split())
        stack = list(map(int,input().split()))
        obj = Solution()
        ans = obj.insertAtBottom(stack,x)
        for e in ans:
            print(e,end=" ")
        print()
        
        
        
# } Driver Code Ends