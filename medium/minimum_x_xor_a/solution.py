# Problem Statement: https://practice.geeksforgeeks.org/problems/1fc4278adf2a36780f637c7b4cd06391dd1487e4/1

#User function Template for python3

class Solution:
    def minVal(self, a, b):
        abit = bin(a)[2:]
        bbit = bin(b)[2:]
        
        temp = []
        
        alen = len(abit)
        
        aco,bco = 0,0
        
        for i in range(alen):
            if abit[i] == "1":
                aco += 1
                temp.append(i)
        
        for ele in bbit:
            if ele == "1":
                bco += 1
               
        if bco > alen:
            return int("".join("1" for i in range(bco)),2)
        
        else:
            ans = [0]*alen
            
            for ele in temp:
                if bco > 0:
                    ans[ele] = 1
                else:
                    break
                bco -= 1
            j = alen-1
            while bco > 0:
                if ans[j] != 1:
                    ans[j] = 1
                    bco -= 1
                j -= 1
        return int("".join(str(ele) for ele in ans),2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a = int(input())
        b = int(input())
        
        ob= Solution()
        print(ob.minVal(a,b))
# } Driver Code Ends