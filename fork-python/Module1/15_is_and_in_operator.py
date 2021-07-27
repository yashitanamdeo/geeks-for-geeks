#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

#Function to find if number is present in the list or not
def number_present(num_list, Q):
    #num is a 'list', Q is a 'int'
    for i in range(len(num_list)):
        if (num_list[i] is Q) :
            return True
    return False 

#{ 
#Driver Code Starts.
def main():
    testcases = int(input())
    while testcases :
        num_list = input()
        num_list = num_list.split()
        for i in range(len(num_list)):
            num_list[i] = int(num_list[i])
        
        q = input()
        q = q.split()
        for i in range(len(q)):
            q[i] = int(q[i])
            
        for i in range(len(q)):
            if number_present(num_list, q[i]):
                print("True")
            else:
                print("False")
        testcases-=1

if __name__ == '__main__' :
    main()
#} Driver Code Ends