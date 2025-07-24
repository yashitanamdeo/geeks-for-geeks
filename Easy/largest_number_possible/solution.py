# Problem Statement: https://practice.geeksforgeeks.org/problems/largest-number-possible5028/1

#User function Template for python3

class Solution:
    def findLargest(self, N, S):
        # code here
        if N!=1 and S==0:   #If N is not a single digit and sum(S) is 0 then not possible, return -1   
            return -1
        elif N==1 and S==0:  #If N is a single digit and sum(S) is 0 then output possible, return 0
            return 0
        else:
            rs=""   #Create an empty string
            while len(rs)!=N:       #Iterate until length of string 'rs' is not equal to N
                if S>9:             #Add largest single digit i.e. 9 if S is not a single digit
                    rs+='9'
                    S-=9            #Reduce the value of sum based on digit assignment to the string
                else:
                    rs+=str(S)      #If sum gets reduced to a value smaller than or equal to 9, then add the digit itself
                    S=0             #The sum remains zero for rest of iteration 
                    
                    
            if S==0:
               return rs 
            else:           #If iteration completes but remaining sum is not zero then output not possible
                return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.findLargest(N, S))
# } Driver Code Ends