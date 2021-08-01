#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

# Function to check value and 
# return accordingly
def check_status(a, b, flag):
    if a == 1 and b == 1:
        return False
    elif flag == True:
        if a < 0 and b < 0:
            return True
    elif a > 0 or b > 0:
        return True
    else:
        return False

#{ 
#Driver Code Starts.

# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        a = int(input())
        b = int(input())
        flag = input()
        
        if(flag == "True"):
            flag = True
        else:
            flag = False
        
        if(check_status(a, b, flag) is True):
            print ("True")
        else:
            print ("False")
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
#} Driver Code Ends