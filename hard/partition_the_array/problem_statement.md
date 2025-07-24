<h1 align="center">Partition the Array</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 62.86%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 21K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>A[] </b>of <b>N </b>integers. The task is to partition the array into four non-empty contiguous subarrays <b>P, Q, R, and S </b>such that each element of the array <b>A[]</b> should be present in any subarray.<br>
Let <b>W, X, Y, and Z</b> be the sum of the elements in <b>P, Q, R, and S</b> respectively.<br>
Find the smallest absolute difference between the maximum and the minimum among<b> W, X, Y, and Z</b>.

<b>Example 1:</b>

<pre><b>Input:
</b>N = 5
A[] = [4,2,2,5,1]
<b>Output: </b>4
<b>Explanation: </b>let partition the array 
P,Q,R,S = [4],[2,2],[5],[1]
W = 4, X = 4, Y = 5, Z = 1 
Differnce = max(W,X,Y,Z)-min(W,X,Y,Z)= 5-1 = 4 </pre>

<b>Example 2:</b>

<pre><b>Input:
</b>N = 4
A[] = {4,4,4,4}
<b>Output: </b>0
<b>Explanation: 
</b>There is only one way to partition 
the array. P,Q,R,S = [4],[4],[4],[4]</pre>

<b>Your Task:</b><br>
You don't need to read input or print anything. The task is to complete the function <b>minDifference</b>() which takes the integer <b>N </b>and the array <b>A[] </b>as inputs and returns the smallest absolute difference.

<b>Expected Time Complexity: </b>O(NLogN)<br>
<b>Expected Auxiliary Space: </b>O(N)

<b>Constraints:</b><br>
4 <u>< </u>N <u>< </u>10<sup>5</sup><br>
1 <u>< </u>A[i] <u>< </u>10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `two-pointer-algorithm` `Arrays` `Binary Search` `Data Structures` `Algorithms`
- **Company Tags:** `None`
