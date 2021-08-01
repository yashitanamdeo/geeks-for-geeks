#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3


def multiplicationTable(N):## in is a membership operator that is true if something is a member of sequence
    for i in range(1,11): ## i in range(x,y,z) means i goes from x to y-1 and increments z steps in each iteration
        print(i * N, end=" ") ## Separating by spaces using end =" "
        

#{ 
#Driver Code Starts.


def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        N = int(input())
        multiplicationTable(N)
        print()
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends