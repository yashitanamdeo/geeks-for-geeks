# Problem Statement: https://practice.geeksforgeeks.org/problems/9656e96f6eaee49e67400fa2aed7833c8d9846b8/1

import collections

class Solution:
    def print_next_greater_freq(self,arr,n):
        res = [-1]*n
        mapp = collections.Counter(arr)
        temp = []
        
        
        for idx, val in enumerate(arr):
            if not temp:
                temp.append(idx)
            else:
                curr = mapp[val]
                while temp:
                    prev_idx = temp[-1]
                    prev_freq = mapp[arr[prev_idx]]
                    if prev_freq < curr:
                        res[prev_idx] = val
                        temp = temp[:len(temp)-1]
                    else:
                        break
                
                temp.append(idx)
                
        return res

#{ 
#  Driver Code Starts
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        obj=Solution()
        ans=obj.print_next_greater_freq(arr,n)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends