#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

def logical(a, b):
    print(a and b) ## do a and b
    print(a or b) ## do a or b
    print(not a) ## do not a


#{ 
#Driver Code Starts.


def main():
    testcases =  int(input()) #testcases
    while(testcases>0):
        a = int(input())
        b = int(input())
        logical(a, b)
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends