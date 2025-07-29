<h1 align="center">Update Queries</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 52.15%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 21K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array of n elements, initially all a[i] = 0. Q queries need to be performed. Each query contains three integers l, r, and x  and you need to change all <b>a[i]</b> to <b>(a[i] | x)</b> for all <b>l ≤ i ≤ r</b>.

Return the array after executing Q queries.

<b>Example 1:</b>

<pre><b>Input:</b>
N=3, Q=2
U=[[1, 3, 1],
   [1, 3, 2]]

<b>Output:</b>
a[]={3,3,3}

<b>Explanation:</b> 
Initially, all elements of the array are 0. After execution of the
first query, all elements become 1 and after execution of the 
second query all elements become 3.</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N=3, Q=2
U=[[1, 2, 1],
   [3, 3, 2]]

<b>Output:</b>
a[]={1,1,2}

<b>Explanantion:</b>
[0,0,0] => [1,1,0] => [1,1,2]</pre>

 

<b>Your Task:  </b><br>
You don't need to read input or print anything. Your task is to complete the function updateQuery<b>()</b> which takes the integer N,Q, and U a QX3 matrix containing the Q queries where U[i][0] is l<sub>i</sub>, U[i][1] is r<sub>i</sub> andU[i][2] is x<sub>i</sub>.and it returns the final array a.

<b>Expected Time Complexity: O(N)<br>
Expected Space Complexity: O(N)</b>

<b>Constraints:</b>

1<=N<=10<sup>5</sup>

1<=Q<=10<sup>5</sup>

1<=U[i][0] <= U[i][1]<=N

1<= U[i][2] <=10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Find Array After Q Queries Where In Each Query Change Ai To Ai X](https://www.geeksforgeeks.org/find-array-after-q-queries-where-in-each-query-change-ai-to-ai-x/)
