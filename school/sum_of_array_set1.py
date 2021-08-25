#User function Template for python3

class Solution:
    def getSum(self, arr, n):
        sum = 0
        for i in range(n):
            sum += arr[i]
        return sum
    
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.getSum(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends