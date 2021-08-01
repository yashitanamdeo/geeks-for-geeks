#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

def checkOddEven(x):
    if(x % 2 == 0):
      # Complete the statement below
      return True
    else:
        # Complete the statement below
        return False

#{ 
#Driver Code Starts.

# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        x = int(input())
        
        if(checkOddEven(x)):
            print ("Even")
        else:
            print ("Odd")
        
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
#} Driver Code Ends