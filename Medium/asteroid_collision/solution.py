# Problem Statement: https://practice.geeksforgeeks.org/problems/asteroid-collision/1

# User function Template for python3

class Solution:
    def asteroidCollision(self, n, arr):
        st = []
        for ele in arr:
            flag = 1
            while st and (st[-1] > 0 and ele < 0):
                if abs(ele) > abs(st[-1]):
                    st.pop()
                elif abs(ele) == abs(st[-1]):
                    flag = 0
                    st.pop()
                    break
                else:
                    flag = 0
                    break
            if flag == 1:
                st.append(ele)
        return st


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        asteroids = list(map(int, input().split()))
        ob = Solution()
        res = ob.asteroidCollision(N, asteroids)
        for val in res:
            print(val, end=' ')
        print()
# } Driver Code Ends
