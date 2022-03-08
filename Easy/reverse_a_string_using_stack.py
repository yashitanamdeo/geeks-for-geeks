# Problem Statement: https://practice.geeksforgeeks.org/problems/reverse-a-string-using-stack/1#

#{ 
#Driver Code Starts

 # } Driver Code Ends
def reverse(S):
    
    #Add code here
    return S[::-1]

#{ 
#Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
#} Driver Code Ends