# Problem Statement: https://practice.geeksforgeeks.org/problems/merge-two-binary-max-heap0144/1#

#User function Template for python3

class Solution():
   def mergeHeaps(self, a, b, n, m):
       '''
       Method 1: Sorting in Desending order
       
        def mergeHeaps(self, a, b, n, m):
            a.extend(b)
            a.sort()
            a.reverse()
            return a
       '''
       #your code here
       self.a=a
       self.b=b
       self.n=n
       self.m=m
       ab=self.a + self.b
       mn=self.n + self.m
       Solution.maxheap(ab,mn)
       return ab
       
   def maxheap(k,mn):
       for i in range((mn//2)-1,-1,-1):
           Solution.heapify(k,mn,i)
   
   def heapify(k,mn,indx):
       if indx >= mn:
           return
       left=(2*indx)+1
       right=(2*indx)+2
       mx=0
       if left < mn and k[left]>k[indx]:
           mx=left
       else:
           mx=indx
       if right < mn and k[right]>k[mx]:
           mx=right
           
       if mx != indx:
           k[mx],k[indx] = k[indx],k[mx]
           Solution.heapify(k,mn,mx)
           
#{ 
#  Driver Code Starts
#Initial Template for Python 3

def isMerged(arr1, arr2, merged):
    if (len(arr1) + len(arr2) != len(merged)):
        return False
    arr1 += arr2
    arr1.sort()
    mergedCopy = sorted(merged)
    if (arr1 != mergedCopy):
        return False
    for i in range(1, len(merged)):
        if merged[i] > merged[(i-1)//2]:
            return False

    return True

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = [int(i) for i in input().split()]
        b = [int(i) for i in input().split()]
        copyA = a[:]
        copyB = b[:]
        obj = Solution()
        merged = obj.mergeHeaps(a, b, n, m)
        flag = isMerged(copyA, copyB, merged)
        print(0 if flag == False else 1)

# } Driver Code Ends