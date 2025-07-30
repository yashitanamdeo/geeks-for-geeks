# Problem Statement: https://practice.geeksforgeeks.org/problems/smallest-absolute-difference4320/1#
# Full test cases were passing from this code


// { Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main(String[] args) throws IOException
	{
	        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int t =
            Integer.parseInt(br.readLine().trim()); // Inputting the testcases
        while(t-->0)
        {
            long n = Long.parseLong(br.readLine().trim());
            long a[] = new long[(int)(n)];
            // long getAnswer[] = new long[(int)(n)];
            String inputLine[] = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                a[i] = Long.parseLong(inputLine[i]);
            }
            long k = Long.parseLong(br.readLine().trim());
            
            Compute obj = new Compute();
            System.out.println(obj.kthDiff(a, n, k));
            
        }
	}
}

// } Driver Code Ends


//User function Template for Java


class Compute {
    
    public long kthDiff(long arr[], long n, long k)
    {
        Arrays.sort(arr);
        int diff= (int) (arr[(int)n-1]-arr[0]);
        int l=0;
        int h=diff;
        while(l<h){
            int m=(l+h)/2;
            if(ok(m,arr,(int)n,(int)k))
                h=m;
            else
                l=m+1;
        }
        return l;
    }
    public static boolean ok(int m,long[] arr,int n,int k){
        int j=1;
        int total=0;
        for(int i=0;i<n;i++){
            while(j<n && arr[j]-arr[i]<=m) j++;
            j--;
            int x=(j-i);
            total+=x;
        }
        return (total>=k);
    }
}