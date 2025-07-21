# Problem Statement: https://practice.geeksforgeeks.org/problems/35bff0ee40090b092e97b02f649085bf1390cc67/1

#User function Template for python3

class Solution:
    def findNumber(self, N: int) -> int:
        # code here

        res_list = []

        odd_list = [1, 3, 5, 7, 9]

        remainder = 0
        quotient = N
        res = 0
        tens = 1

        while quotient:
            remainder = quotient % 5
            quotient = quotient//5
            if remainder == 0:
                res_list.append(odd_list[4])
                quotient -= 1

            else:
                res_list.append(odd_list[remainder - 1])

        for i in res_list:
            res += i * tens
            tens *= 10

        return res


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        N = int(input())

        obj = Solution()
        res = obj.findNumber(N)

        print(res)

# } Driver Code Ends
