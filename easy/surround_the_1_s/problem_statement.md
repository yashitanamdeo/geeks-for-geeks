<h1 align="center">Surround the 1's</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 54.02%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 43K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 10m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a matrix of order <b>n</b>x<b>m</b>, composed of only 0's and 1's, find the number of 1's in the matrix that are surrounded by an <b>even number (>0) of 0's</b>. The surrounding of a cell in the matrix is defined as the <b>elements above</b>, <b>below</b>, on <b>left</b>, on <b>right</b> as well as the<b> 4 diagonal elements</b> around the cell of the matrix. Hence, the surrounding of any matrix elements is composed of 8 elements. Find the number of such 1's.

<b>Example 1:</b>

<pre><b>Input: <br></b>matrix = {{1, 0, 0}, <br>          {1, 1, 0}, 
          {0, 1, 0}}
<b>Output: <br></b>1
<b>Explanation: <br></b>1 that occurs in the 1st row and 1st column, has 3 surrounding elements 0,1 and 1. The occurrence of zero is odd. <br>1 that occurs in 2nd row and 1st column has 5 surrounding elements 1,0,1,1 and 0. The occurrence of zero is even. <br>1 that occurs in 2nd row and 2nd column has 8 surrounding elements. The occurrence of 0 is odd. <br>Similarly, for the 1 that occurs in 3rd row and 2nd column, the occurrence of zero in it's 5 surrounding elements is odd. 
Hence, the output is 1.
</pre>

<b>Example 2:</b>

<pre><b>Input: <br></b>matrix = {{1}}
<b>Output: <br></b>0
<b>Explanation: <br></b>There is only 1 element in the matrix. Hence, it has no surroundings, so it's count for even 0's is 0 for the whole matrix. <br>0 is even but we want occurrence of a zero in the surrounding at least once. 
Hence, output is 0.
</pre>

<b>Your Task:</b><br>You don't need to read or print anything. Your task is to complete the function <b>Count()</b> which takes the matrix as input parameter and returns the number of 1's which are surrounded by even number of 0's.

<b>Expected Time Complexity: </b>O(n * m)<br><b>Expected Space Complexity: </b>O(1)

<b>Constraints:</b><br>1 <= n, m <= 10<sup>3</sup>


<hr>

### Tags
- **Topic Tags:** `Matrix` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Counting 1s Surrounded By Even 0s](https://www.geeksforgeeks.org/counting-1s-surrounded-by-even-0s/)
