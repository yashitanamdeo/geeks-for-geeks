# Problem Statement: https://practice.geeksforgeeks.org/problems/sum-of-two-numbers-without-using-arithmetic-operators/1

#User function Template for python3

def sum(a,b):
    #code here
    result = 0
    carry = a & b

    if carry:
        result = a ^ b
        carry = carry << 1
        result = sum(carry, result)
   
    else:
        result = a ^ b

    return result

#{ 
#  Driver Code Starts
import math
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        inp = list(map(int,input().split())) 
        
        a=inp[0]
        b=inp[1]
        
        #ob=Solution()
        print(sum(a,b))
     
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends