#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

def comparison(a, b):
    print(a==b) ##do a==b
    print(a>b) ##do a>b
    print(a!=b) ##do a!=b
    print(a<b) ##do a<b

#{ 
#Driver Code Starts.





def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        b=int(input())
        comparison(a,b)
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends