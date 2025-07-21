# Problem Statement: https://practice.geeksforgeeks.org/problems/230d87552a332a2970b2092451334a007f2b0eec/1

#User function Template for python3


class Solution:
    def carpetBox(self, a, b, c, d):
        a, b = min(a, b), max(a, b)
        c, d = min(c, d), max(c, d)
        if (a <= c and b <= d) or (a <= d and b <= c):
            return 0
        if (a > c and b <= d):
            return 1 + self.carpetBox(a//2, b, c, d)
        else:
            return 1 + self.carpetBox(a, b//2, c, d)


#{
 # Driver Code Starts
#Initial Template for Python 3

def main():
    T = int(input())
    while(T > 0):
        A, B, C, D = map(int, input().split())

        obj = Solution()
        print(obj.carpetBox(A, B, C, D))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
