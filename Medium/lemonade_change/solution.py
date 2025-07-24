# Problem Statement: https://practice.geeksforgeeks.org/problems/lemonade-change/1

# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3

class Solution:
    def lemonadeChange(self, N, bills):
        d = {5: 0, 10: 0, 20: 0}
        for i in bills:
            k = i-5
            while (k > 0):
                if (k >= 20 and d.get(20) > 0):
                    d[20] = d.get(20)-1
                    k -= 20
                elif (k >= 10 and d.get(10) > 0):
                    d[10] = d.get(10)-1
                    k -= 10
                elif (k >= 5 and d.get(5) > 0):
                    d[5] = d.get(5)-1
                    k -= 5
                else:
                    return False
            d[i] = d.get(i)+1
        return True


# {
 # Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        bills = list(map(int, input().split()))
        ob = Solution()
        res = ob.lemonadeChange(N, bills)
        print(res)
# } Driver Code Ends
