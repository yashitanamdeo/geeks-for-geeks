# Problem Statement: https://practice.geeksforgeeks.org/problems/45fa306a9116332ece4cecdaedf50f140bd252d4/1

class Solution:
    def maxInstance(self, s: str) -> int:
        td = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for i in s:
            if i in td:
                td[i] += 1
        td['l'] = td['l']//2
        td['o'] = td['o']//2
        return(min(td.values()))


#{
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.maxInstance(s)

        print(res)

# } Driver Code Ends
