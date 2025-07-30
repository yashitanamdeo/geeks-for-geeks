<h1 align="center">Longest Perfect Piece</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.16%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 19K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[]</b> of <b>N</b> Numbers. A Perfect Piece is defined as a subarray such that the difference between the minimum and the maximum value in that range is<b> </b>at most 1. Find the Maximal Length Perfect Piece.

 

<b>Example 1:</b>

<pre><b>Input:</b>
<b>N = </b>4
<b>arr[] = </b>{8, 8, 8, 8}
<b>Output:
</b>4
<b>Explanation:</b>
The longest subarray is [1, 4]
where maximum=8 and minimum = 8 and
difference is 0, which is less than 1.
Its length is 4.</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
<b>N = </b>11
<b>arr[] = </b>{5, 4, 5, 5, 6, 7, 8, 8, 8, 7, 6}
<b>Output:
</b>5
<b>Explanation:</b>
The longest subarray is [6, 10]
where maximum=8 and minimum = 7 and
difference is 1. Its length is 5. </pre>

 

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>longestPerfectPiece()</b> which takes an Integer N and an array arr[] of length N as input and returns the maximal length Perfect Piece.

 

<b>Expected Time Complexity:</b> O(N*logN)<br><b>Expected Auxiliary Space:</b> O(N)

 

<b>Constraints:</b><br>1 <= N <= 10<sup>5</sup><br>1 <= arr[i] <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Pointers` `Algorithms`
- **Company Tags:** `None`
