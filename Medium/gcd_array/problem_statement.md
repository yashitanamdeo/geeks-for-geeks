<h1 align="center">GCD Array</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 62.54%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 15K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array, <b>arr </b>of length <b>N</b>, and also a single integer <b>K </b>. Your task is to split the array arr into <b>K </b>non-overlapping, non-empty subarrays. For each of the subarrays, you calculate the sum of the elements in it. Let us denote these sums as <b>S<sub>1</sub>,<sub> </sub>S<sub>2</sub>, S<sub>3</sub>, ..., S<sub>K</sub></b>. Where <b>S<sub>i </sub></b>denotes the sum of the elements in the i<sup>th </sup>subarray from left.

Let <b>G = GCD( S<sub>1</sub>,<sub> </sub>S<sub>2 </sub>,S<sub>3 </sub>, ...,<sub> </sub>S<sub>K</sub>)</b>.

Find the <b>maximum </b>value of G that can be obtained. <br>
The array may contain duplicate elements.

<b>Example 1:</b>

<pre><b>Input</b>:
N = 5
K = 4
arr[] = {6, 7, 5, 27, 3}
<b>Output:</b> 3
<b>Explanation</b>: 
Since K = 4, you have to split the array into 4 subarrays.
For optimal splitting, split the array into
4 subarrays as follows: [[6], [7, 5], [27], [3]]
Therefore, S<sub>1</sub> = 6, S<sub>2</sub> = 7 + 5 = 12, S<sub>3</sub> = 27, S<sub>4</sub> = 3
Hence, G = GCD(S<sub>1</sub>, S<sub>2</sub>, S<sub>3</sub>, S<sub>4</sub>) = GCD(6, 12, 27, 3) = 3
It can be shown that 3 is the maximum value of G that can be obtained.
Thus, the answer is 3.</pre>

<b>Example 2:</b>

<pre><b>Input</b>:
N = 3
K = 2
arr[] = {1, 4, 5}
<b>Output:</b> 5
<b>Explanation</b>: 
Since K = 2, you have to split the array into 2 subarrays.
For optimal splitting, split the array into
2 subarrays as follows: [[1, 4], [5]]
Therefore, S<sub>1</sub> = 1 + 4 = 5, S<sub>2</sub> = 5
Hence, G = GCD(S<sub>1</sub>, S<sub>2</sub>) = GCD(5,5) = 5
It can be shown that 5 is the maximum value of G that can be obtained.
Thus, the answer is 5.</pre>

<br>
<b>Your Task:  </b><br>
You don't need to read input or print anything. Your task is to complete the function <b>solve()</b> which takes the array arr[] and its size N and an integer K as input parameters and returns the required maximum GCD value.<br>
 

<b>Expected Time Complexity: </b>O(N * x)<br>
<b>Expected Auxiliary Space: </b>O(x), x is the number of factors of the sum of all elements.<br>
<br>
<b>Constraints:</b>

1 <= N <= 10<sup>4</sup><br>
1 <= K <= N<br>
1 <= arr[i] <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Mathematical` `Data Structures` `Algorithms`
- **Company Tags:** `None`
