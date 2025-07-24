# Problem Statement: https://practice.geeksforgeeks.org/problems/jumping-numbers3805/1

#User function Template for python3

from collections import deque
class Solution:
    def jumpingNums(self, X):
        arr = deque([1,2,3,4,5,6,7,8,9])
        if X in range(10): return X
        else:
            last = 9
            while arr:
                ele = arr.popleft()
                if ele%10 != 0 and ele%10 != 9:
                    new_ele_1 = ele*10+(ele%10)-1
                    new_ele_2 = ele*10+(ele%10)+1
                    if X >= new_ele_2: 
                            last = new_ele_2
                            arr.extend([new_ele_1,new_ele_2])
                    else:
                        if X >= new_ele_1:
                            last = new_ele_1
                            arr.append(new_ele_1)
                        else:
                            return last
                elif ele%10 == 0:
                    new_ele = ele*10+(ele%10)+1
                    if  X >= new_ele:
                        last = new_ele
                        arr.append(new_ele)
                    else:
                        return last
                else:
                    new_ele = ele*10+(ele%10)-1
                    if  X >= new_ele:
                        last = new_ele
                        arr.append(new_ele)
                    else:
                        return last


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.jumpingNums(X))
# } Driver Code Ends