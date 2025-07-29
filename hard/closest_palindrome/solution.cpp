// Problem Statement: https://practice.geeksforgeeks.org/problems/closest-palindrome4519/1#

// { Driver Code Starts

#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends

long long int N = 0;

bool comp(long long int a, long long int b) {
    return abs(N-a) < abs(N-b);
}

class Solution {
public:
    long long int mkPal(long long int num) {
        string s = to_string(num);
        int n = s.length();
        
        for(int i=0; i<n/2; i++)
            s[n-i-1] = s[i];
        
        stringstream ss(s); ss>>num;
        return num;
    }
    
	long long int closestPalindrome(long long int num){
	    long long int d = (to_string(num)).length();
	    if(d == 1) return num;
	    
	    N = num;
	    long long int ans[4] = {0};
	    ans[0] = mkPal(num-pow(10ll, (d-1)/2));
	    ans[1] = mkPal(num-pow(10ll, d/2));
	    ans[2] = mkPal(num);
	    ans[3] = mkPal(num+pow(10ll, d/2));
	    
	    sort(ans, ans+5, comp);
	    
	    return ans[0];
	}

};


// { Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		long long int num;
		cin >> num;
		Solution obj;
		long long int ans = obj.closestPalindrome(num);
		cout << ans <<"\n";
	}
	return 0;
}  // } Driver Code Ends