<h1 align="center">Positive Negative Pair</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 39.3%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 42K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of distinct integers, find all the pairs having both negative and positive values of a number in the array.

<br>
<b>Example 1:</b>

<pre><b>Input:
</b>n = 8
arr[] = {1,3,6,-2,-1,-3,2,7}
<b>Output: </b>-1 1 -3 3 -2 2<b>
Explanation: </b>1, 3 and 2 are present 
pairwise positive and negative. 6 and 
7 have no pair.
</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>n = 3
arr[] = {3,2,1}
<b>Output: </b>0<b>
Explanation: </b>No such pair exists so the 
output is 0.</pre>

<br>
<b>Your Task:</b><br>
You do not need to read input or print anything. Complete the function <b>findPairs()</b> which takes the array A[] and the size of the array, n, as input parameters and returns a list of integers denoting the pairs. The pair that appears first(i.e. second element of the pair appears first) in A[] should appear first in the returning list and within the pair, the negative integer should appear before the positive integer. Return an empty integer list if no such pair exists. 

<br>
<b>Expected Time Complexity: </b>O(n)<br>
<b>Expected Auxiliary Space:</b> O(n)

<br>
<b>Constraints:</b><br>
1 <= n <= 10<sup>6</sup><br>
-10<sup>6</sup> <= arr[i] <= 10<sup>6</sup>


<hr>

### Tags
- **Topic Tags:** `Hash` `Data Structures`
- **Company Tags:** `Amazon`

### Related Articles
- [Pairs Of Positive Negative Values In An Array](https://www.geeksforgeeks.org/pairs-of-positive-negative-values-in-an-array/)
