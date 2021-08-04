#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

def doge_count(str):
    count = 0
    for i in range(0, len(str)-3):
        if str[i] == "d" and str[i+1] == "o" and str[i+3] == "e":
            count = count+1
    return count

#{ 
#Driver Code Starts.



def main():
    testcases = int(input()) #testcases
    while(testcases > 0):
        str = input()
        print(doge_count(str))
        testcases -= 1
        


if __name__=='__main__':
    main()
#} Driver Code Ends