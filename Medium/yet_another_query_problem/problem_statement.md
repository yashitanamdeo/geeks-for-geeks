<h1 align="center">Yet another query problem</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 63.05%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 18K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array of <b>N</b> elements and <b>num</b> queries, In each query you are given three numbers L,R and K and you have to tell, how many indexes are there in between L and R(L<=i<=R) such that the frequency of a[i] from index i to n-1 is k.

<b>Note:</b> 0-based indexing

<b>Example 1:</b>

<pre><b>Input:</b>
N=5
num=3
A={1,1,3,4,3}
Q={{0,2,2},{0,2,1},{0,4,2}}
<b>Output:</b>
2 1 2
<b>Explanation:</b>
For query 1: 0 2 2
L=0,R=2,K=2
let, L<=i<=R
For i=0: frequency of a[i] i.e. 1 from i to n-1 is 2.
For i=1: frequency of a[i] i.e. 1 from i to n-1 is 1.
For i=2: frequency of a[i] i.e. 3 from i to n-1 is 2.
Hence we have <b>two</b> elements from index 0 to 2 
whose frequency from i to n-1 is 2.

For query 2: 0 2 1
L=0,R=2,K=1
As we can see from the above query that there is 
only a single element in 0 to 2 whose frequency 
from i to n-1 is 1.

For query 3: 0 4 2
The answer will be 2 because of the index 0 and 2.</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N=5
num=2
A={1,1,1,1,1}
Q={{0,4,2},{0,4,1}}
<b>Output:</b>
1 1 
<b>Explanation:</b> 
For query 1: 0 4 2 
L=0,R=4,K=2 
let, L<=i<=R 
For i=0: frequency of a[i] i.e. 1 from i to n-1 is 5. 
For i=1: frequency of a[i] i.e. 1 from i to n-1 is 4. 
For i=2: frequency of a[i] i.e. 1 from i to n-1 is 3.
For i=3: frequency of a[i] i.e. 1 from i to n-1 is <b>2</b>.
For i=4: frequency of a[i] i.e. 1 from i to n-1 is 1. 
Hence we have <b>one</b> elements from index 0 to 4 whose frequency from i to n-1 is 2. 

Similarly For query 2: 
there is only 1 element in 0 to 4 whose frequency from i to n-1 is 1.
</pre>

<b>Expected Time Complexity:</b> O(N<sup>2</sup>)<br>
<b>Expected Auxiliary Space:</b> O(N<sup>2</sup>)

<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function solveQueries() which take two variable <b>N</b> and <b>num</b> representing the length of the original array and number of queries and two arrays as input, <b>A</b> and <b>Q</b> representing the original array and an array of queries(2-D array with 3 columns of<b> L</b>,<b>R</b> and <b>K </b>respectively), and returns the array of length <b>num </b>with the solution to each query.<br>
 

<b>Constraints:</b><br>
1 <= N <= 10<sup>3</sup><br>
0 <= Q < 10<sup>3</sup><br>
1 <= A[i] <= 10<sup>5</sup>

<br>
<b> </b>


<hr>

### Tags
- **Topic Tags:** `prefix-sum` `Arrays` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Count Indices With Specific Frequency In Array Range](https://www.geeksforgeeks.org/count-indices-with-specific-frequency-in-array-range/)
