#User function Template for python3

def inPutS():
    string = input() ## input in a single line()
    s, i, f = string.split(" ")## split the a into three parts: string, integer, and f. 
    print(s + " " + str(int(i) + float(f))) ##type cast i to int, f to float. Add i with f. Typecast the result to string

#{ 
#  Driver Code Starts

def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        inPutS() #the function that gets things done
        testcases-=1
        


if __name__=='__main__':
    main()
# } Driver Code Ends