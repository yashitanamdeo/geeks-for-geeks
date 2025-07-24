<h1 align="center">Solve the Sudoku</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 37.98%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 123K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 60m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an incomplete [<b>Sudoku</b>](https://www.geeksforgeeks.org/introduction-to-sudoku-puzzles-and-how-to-solve-them/) configuration in terms of a 9x9  2-D interger square matrix, <b>mat[][]</b>, the task is to solve the Sudoku. It is <b>guaranteed </b>that the input Sudoku will have exactly <b>one </b>solution.

A sudoku solution must satisfy all of the following rules:

1. Each of the digits 1-9 must occur exactly once in each row.
1. Each of the digits 1-9 must occur exactly once in each column.
1. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
<b>Note:</b> Zeros represent blanks to be filled with numbers 1-9, while non-zero cells are <b>fixed </b>and cannot be changed.<br>

<b>Examples:</b>

<pre><b>Input: </b>mat[][] = 

<b>Output:</b>
<br><b>Explanation:</b> Each row, column and 3 x 3 box of the output matrix contains unique numbers.</pre>

<pre><b>Input: </b>mat[][] = 
<br><b>Output:</b><br><br><b>Explanation:</b> Each row, column and 3 x 3 box of the output matrix contains unique numbers.</pre>

<b>Constraints:</b><br>mat.size() = 9<br>mat[i].size() = 9<br>0 ≤ mat[i][j] ≤ 9<br>

## Expected Complexities
- Time Complexity: O(9 ^ (n * n))
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Matrix` `Backtracking` `Data Structures` `Algorithms`
- **Company Tags:** `Zoho` `Flipkart` `Amazon` `Microsoft` `MakeMyTrip` `Ola Cabs` `Oracle` `MAQ Software` `Directi` `PayPal` `Samsung`

### Related Articles
- [Sudoku Backtracking 7](https://www.geeksforgeeks.org/sudoku-backtracking-7/)

### Related Interview Experiences
- [Ola Interview Experience Set 8 For Sde 2](https://www.geeksforgeeks.org/ola-interview-experience-set-8-for-sde-2/)
- [Makemytrip Interview Experience Set 10 On Campus](https://www.geeksforgeeks.org/makemytrip-interview-experience-set-10-on-campus/)
- [Microsoft Interview Experience For Sde 1 2](https://www.geeksforgeeks.org/microsoft-interview-experience-for-sde-1-2/)
