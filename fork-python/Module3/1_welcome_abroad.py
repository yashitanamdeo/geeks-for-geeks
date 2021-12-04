'''Problem Statement:https://practice.geeksforgeeks.org/problems/welcome-aboard-python/1/?track=python-module-3&batchId=119'''

#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

# Function to Welcome the person
def welcomeAboard(name):
    print("Welcome", name) # Your code here
   

#{ 
#Driver Code Starts.
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        name = input()
        
        welcomeAboard(name);
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
#} Driver Code Ends