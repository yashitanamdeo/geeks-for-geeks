# Problem Statement: https://www.geeksforgeeks.org/problems/help-nobita0532/1


class Solution:
    def oddEven(self, s : str) -> str:
        # code here
        m = {}
        
        for c in s:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1
        
        x = 0
        y = 0
        
        for it in m:
            
            pos = ord(it) - ord('a') + 1
            
            if pos % 2 == 0 and m[it] % 2 == 0:
                x +=1
            elif pos % 2 != 0 and m[it] % 2 != 0:
                y += 1

        if (x + y) % 2 == 0:
            return "EVEN"
        
        return "ODD"
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends