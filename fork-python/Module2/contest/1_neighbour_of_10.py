#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

def isNeighbour(N):
    return (N + 2) % 10 <= 4 #can add upto 2 or substract upto 2 so 4


#{ 
#Driver Code Starts.



def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        N = int(input())
        print(isNeighbour(N))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends