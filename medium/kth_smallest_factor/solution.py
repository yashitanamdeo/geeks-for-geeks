# Problem Statement: https://practice.geeksforgeeks.org/problems/kth-smallest-factor2345/1

# In python
#User function Template for python3

class Solution:
    def kThSmallestFactor(self, N , K):
        # code here 
        factorsList = []
        for i in range(1,N+1):
            if N%i == 0:
                factorsList.append(i)
                
        if K > len(factorsList):
            return -1
        
        return factorsList[K-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        
        ob = Solution()
        print(ob.kThSmallestFactor(N,K))
# } Driver Code Ends



# In Java
'''
// { Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            String S[] = read.readLine().split(" ");
            
            int N = Integer.parseInt(S[0]);
            int K = Integer.parseInt(S[1]);

            Solution ob = new Solution();
            System.out.println(ob.kThSmallestFactor(N,K));
        }
    }
}// } Driver Code Ends


//User function Template for Java

class Solution {
    static int kThSmallestFactor(int N , int K) {
        int fact=0;
        for(int i=1;(i<=N);i++){
            if(N%i==0){
                fact++;
            }
            if(K==fact){
                return i;
            }
        }
        return -1;
    }
};
'''