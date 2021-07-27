#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

# Function to perform mathematical operation on X and Y
def do_operation(X, Y):
    # Your code here
    print(X + Y)
    print(X - Y)
    print(X * Y)
    print(X / Y)
    print(X ** Y)
    print(X // Y)

#{ 
#Driver Code Starts.

# Python Code to perform mathematical operation
def main():
    testcase = int(input())
    
    while(testcase > 0):
        input1 = input().split()
        X = int(input1[0])
        Y = int(input1[1])
        do_operation(X, Y)
        
        testcase -= 1
        

if __name__ == '__main__':
    main()
    
#} Driver Code Ends