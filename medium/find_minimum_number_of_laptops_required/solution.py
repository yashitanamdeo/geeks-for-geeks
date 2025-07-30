# Problem Statement: https://practice.geeksforgeeks.org/problems/af49b143a4ead583e943ca6176fbd7ea55b121ae/1

#User function Template for python3

import heapq
class Solution: 
    def minLaptops(self, N, start, end):
        lst=list(zip(start,end))
        lst.sort(key=lambda x:(x[0],x[1]))
        st=[]
        heapq.heapify(st)
        mx=0
        for i in range(N):
            if st==[]:
                heapq.heappush(st,lst[i][1])
                # st.append(lst[i][1])
            else:
                x=heapq.heappop(st)
                if x>lst[i][0]:
                    heapq.heappush(st,x)
                heapq.heappush(st,lst[i][1])
            mx=max(mx,len(st))
        return mx


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N = int(input())
        start = list(map(int,input().split()))
        end = list(map(int,input().split()))
            
        ob = Solution()
        print(ob.minLaptops(N, start, end))
        
        T -= 1

# } Driver Code Ends