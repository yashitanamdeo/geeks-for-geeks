# Problem Statement: https://practice.geeksforgeeks.org/problems/anagram-of-string/1#

# function to calculate minimum numbers of characters
# to be removed to make two strings anagram
def remAnagram(str1,str2):
    #print(str1)
    #print(str2)
    s1=[x for x in str1]
    s2=[x for x in str2]
    count=0
    i=0
    while i<=len(s1)-1:
        char=s1[i]
        if char not in  s2:
            s1.remove(char)
            count+=1
            #print(s1)
            continue
        s1.remove(char)
        s2.remove(char)
    i=0
    while i<= len(s2)-1:
        char=s2[i]
        if char not in  s1:
            s2.remove(char)
            count+=1
            continue
        s1.remove(char)
        s2.remove(char)
    return count

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        str2=input()
        print(remAnagram(str1,str2))
# } Driver Code Ends