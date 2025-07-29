<h1 align="center">Unique rows in boolean matrix</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 48.36%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 52K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary matrix your task is to find all unique rows of the given matrix in the order of their appearance in the matrix. 

<b>Example 1:</b>

<pre><b>Input:
</b>row = 3, col = 4 
M[][] = {{1 1 0 1},{1 0 0 1},{1 1 0 1}}
<b>Output: </b>$1 1 0 1 $1 0 0 1 $<b>
Explanation: </b>Above the matrix of size 3x4
looks like
1 1 0 1
1 0 0 1
1 1 0 1
The two unique rows are R<sub>1</sub>: {1 1 0 1} and R<sub>2</sub>: {1 0 0 1}. <br>As R<sub>1 </sub>first appeared at row-0 and R<sub>2</sub> appeared at row-1, in the resulting list, R<sub>1</sub> is kept before R<sub>2</sub>.</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>row = 2, col = 4 
M[][] = {{0 0 0 1}, {0 0 0 1}}
<b>Output: $</b>0 0 0 1 $<b>
Explanation: </b>Above the matrix of size 2x4
looks like
0 0 0 1
0 0 0 1
Only unique row is $0 0 0 1 $</pre>

<b>Your Task:</b><br>You only need to implement the given function <b>uniqueRow()</b>. The function takes three arguments the first argument is a matrix <b>M</b> and the next two arguments are <b>row</b> and <b>col</b> denoting the rows and columns of the matrix. The function should <b>return</b> the list of the unique row of the matrix. Do not read input, instead use the arguments given in the function.

<b>Note: </b>The driver code prints the rows "$" separated. You have to just return list of rows, you do not have to worry about printing anything.

<b>Expected Time Complexity:</b> O(row * col)<br><b>Expected Auxiliary Space:</b> O(row * col)

<b>Constraints:</b><br>1<=row,col<=40<br>0<=M[][]<=1


<hr>

### Tags
- **Topic Tags:** `set` `Matrix` `Trie` `Data Structures` `Advanced Data Structure`
- **Company Tags:** `Zoho` `Amazon`

### Related Articles
- [Print Unique Rows](https://www.geeksforgeeks.org/print-unique-rows/)
