# Problem Statement: https://practice.geeksforgeeks.org/problems/a4f19ea532cee502aabec77c07e0d0a45b76ecf9/1

class Solution:
    def build_bridges(self, text1, text2):
        dp = [[0] * len(text2) for i in range(len(text1))]
        
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j] , dp[i][j - 1])
                    
        return dp[-1][-1]


#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        obj = Solution()
        str1, str2 = input().split()
        print(obj.build_bridges(str1, str2))

# } Driver Code Ends