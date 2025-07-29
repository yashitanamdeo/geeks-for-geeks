<h1 align="center">Binary matrix having maximum number of 1s</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 60.93%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 25K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary matrix (containing only <b>0</b> and <b>1</b>) of order NxN. <b>All rows are sorted already</b>, We need to find the row number with the <b>maximum number of 1s</b>. Also, find the number of 1s in that row.<br>
<b>Note:</b>

1.<b> </b>In case of a tie, print the smaller row number.<br>
2. Row number should start from 0<sup>th</sup> index.

<b>Example 1</b>

<pre><b>Input:
</b>N=3
mat[3][3] = {0, 0, 1, 
              0, 1, 1, 
              0, 0, 0}
<b>Output:</b>
Row number = 1
MaxCount = 2
<b>Explanation:</b>
Here, max number of 1s is in row number 1
and its count is 2.</pre>

<b>Example 2</b>

<pre><b>Input:
</b>N=3
mat[3][3] = {1, 1, 1, 
              1, 1, 1, 
              0, 0, 0}
<b>Output:</b>
Row number = 0
MaxCount = 3</pre>

<b>Your Task:</b><br>
You don't need to read input or print anything. The task is to complete the function <b>findMaxRow()</b> which takes mat[][] as the 2D matrix and N as the size of matrix. Your task is to find the row number with the <b>maximum number of 1s </b>and find the number of 1s in that row and return the answer in a vector of size 2 where at 0<sup>th </sup>index will be the row number and at 1<sup>th </sup>index will be MaxCount.

<b>Expected Time Complexity:</b> O(N)<br>
<b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>
1 <= N <= 10<sup>3</sup><br>
0 <= mat[][]<= 1


<hr>

### Tags
- **Topic Tags:** `Binary Search` `Algorithms`
- **Company Tags:** `Swiggy`

### Related Articles
- [Find Row Number Binary Matrix Maximum Number 1s](https://www.geeksforgeeks.org/find-row-number-binary-matrix-maximum-number-1s/)

### Related Interview Experiences
- [Swiggy Interview Experience For Sde 1 Off Campus 2021](https://www.geeksforgeeks.org/swiggy-interview-experience-for-sde-1-off-campus-2021/)
