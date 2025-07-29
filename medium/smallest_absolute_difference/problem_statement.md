<h1 align="center">Smallest Absolute Difference</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 29.83%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 17K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of size <b>n</b> containing positive integers n and a number <b>k</b>,The absolute difference between values at indices i and j is <b>|a[i] - a[j]|</b>. There are <b>n*(n-1)/2</b> such pairs and you have to print the <b>k<sub>th</sub></b> <b>smallest</b> <b>absolute</b> <b>difference</b> among all these pairs.

<b>Examples :</b>

<pre><b>Input : </b>n = 4, a[] = {1, 2, 3, 4},  = 3<b>
Output : </b>1 <b>
Explanation : </b>The possible absolute differences are : {1, 2, 3, 1, 2, 1}. The 3rd smallest value among these is 1.</pre>

<pre><b>Input : </b>n = 2, a[] = {10, 10}, k = 1
<b>Output : </b>0</pre>

<br><b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>kthDiff()</b> which takes the array <b>a[]</b>, its size <b>n </b>and an integer <b>k </b>as inputs and returns the <b>k<sub>th</sub></b> smallest absolute difference among all these pairs.

<b>Expected Time Complexity:</b> O( N. (Log(n))<sup>2</sup> )<br><b>Expected Auxiliary Space:</b> O(Log(n))

<b>Constraints:</b><br>1<=n<=10<sup>5</sup><br>1<=a[i]<=10<sup>5</sup><br>1 <= k <= n*(n-1)/2


<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [K Th Smallest Absolute Difference Two Elements Array](https://www.geeksforgeeks.org/k-th-smallest-absolute-difference-two-elements-array/)
