# Problem Statement: https://www.geeksforgeeks.org/problems/first-element-to-occur-k-times5150/1

#User function Template for python3


class Solution:
    def firstElementKTime(self, n, k, a):
        count_dict = {}
        for num in a:
            count_dict[num] = count_dict.get(num, 0) + 1
            if count_dict[num] == k:
                return num
        return -1
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstElementKTime(n, k, a))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends