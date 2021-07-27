#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3


def bitwise(a, b, c):
    e = c ^ b
    print(a ^ a)
    print(c ^ b)
    print(a & b)
    print(c | (a ^ a))
    print(~e)

#{ 
#Driver Code Starts.



def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a = int(input())
        b = int(input())
        c = int(input())
        bitwise(a, b, c)
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends