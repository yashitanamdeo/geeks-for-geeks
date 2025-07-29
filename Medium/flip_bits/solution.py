# Problem Statement: https://practice.geeksforgeeks.org/problems/flip-bits0240/1

#User function Template for python3

class Solution:
    def maxOnes(self, a, n):
        ones=0
        count=0
        max_count=0
        for e in a:
            if e==0:
                if count>=0:
                    count+=1
                else:
                    count=1
            else:
                ones+=1
                count-=1
            max_count=max(max_count,count)
        return ones+max_count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.maxOnes(a, n))

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends