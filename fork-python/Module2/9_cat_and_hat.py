#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

def cat_hat(str):
    return str.count('cat')==str.count('hat')

# Alternative Solution
def cat_hat(str):
    cat = 0
    hat = 0
    for i in range(0,len(str)-2):
        if str[i:i+3] == 'cat':
            cat+=1
        if str[i:i+3] == 'hat':
            hat+=1
    return cat == hat
   
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
