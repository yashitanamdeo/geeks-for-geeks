#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

def cat_hat(str):
    return str.count('cat')==str.count('hat')

#{ 
#Driver Code Starts.




def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str = input()
        print(cat_hat(str))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends