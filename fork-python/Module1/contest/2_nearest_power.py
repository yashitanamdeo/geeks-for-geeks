#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

    
def nearestPower(A, B):
    x=math.floor(math.log(B,A))
    xPlusOne=x+1
    number1=A**x
    number2=A**xPlusOne
    if(abs(number1-B)>abs(number2-B)):
        return number2
    else:
        return number1
#{ 
#Driver Code Starts.


import math

    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        A = int(input())
        B = int(input())
        print(nearestPower(A, B))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends