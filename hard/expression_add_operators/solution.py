# Problem Statement: https://practice.geeksforgeeks.org/problems/expression-add-operators/1

#User function Template for python3

class Solution:
    def addOperators(self, s, target):
        n = len(s)
        ans = []
        def dfs(i, path, result, prev):
            if i == n:
                if result == target:
                    ans.append(path)
                return

            for j in range(i+1, n+1):
                if j > i+1 and s[i] == '0': 
                    break  
                num = int(s[i:j])
                if i == 0:
                    dfs(j, path + str(num), result + num, num)  
                else:
                    dfs(j, path + "+" + str(num), result + num, num)
                    dfs(j, path + "-" + str(num), result - num, -num)
                    dfs(j, path + "*" + str(num), result - prev + prev*num, prev*num)  

        ans = []
        dfs(0, "", 0, 0)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        S = input()
        target = int(input())
        ob = Solution()
        res = ob.addOperators(S, target)
        res.sort()
        for combination in res:
            print(combination, end = ' ')
        print()
# } Driver Code Ends
