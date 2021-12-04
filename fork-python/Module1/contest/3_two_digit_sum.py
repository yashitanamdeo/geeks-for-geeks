#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

def digitsSum(N):
    ##Your code here
    sum = 0
    for digit in str(N):  
      sum += int(digit)       
    return sum

#{ 
#Driver Code Starts.




def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        N = int(input())
        print(digitsSum(N))
        testcases -= 1
        


if __name__=='__main__':
    main()
#} Driver Code Ends
