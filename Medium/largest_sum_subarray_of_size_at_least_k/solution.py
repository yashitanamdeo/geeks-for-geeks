# Problem Statement: https://www.geeksforgeeks.org/problems/largest-sum-subarray-of-size-at-least-k3121/1

#User function Template for python3

class Solution():
    def maxSumWithK(self, a, n, k):
        # Code here
        ans=float('-inf')
        total=0
        last=0
        j=0
        for i in range(n):
            total+=a[i]
            if(i-j+1==k):
                ans=max(ans,total)
            elif(i-j+1>k):
                last+=a[j]
                j+=1
                if (last<0):
                    total-=last
                    last=0
                ans=max(ans,total)
        return ans
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.maxSumWithK(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends