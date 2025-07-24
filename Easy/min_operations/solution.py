# Problem Statement: https://practice.geeksforgeeks.org/problems/5a7e1a52f1b7796238f9efea4c6fda389f26c327/1

class Solution:
    def solve(self, a : int, b : int) -> int:
        # code here
        if a==b:
            return 0
        elif a&b ==a or a&b==b:
            return 1
        else:
            return 2
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a = int(input())
        
        
        b = int(input())
        
        obj = Solution()
        res = obj.solve(a, b)
        
        print(res)
        

# } Driver Code Ends