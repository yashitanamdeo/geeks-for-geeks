<h1 align="center">Juggler Sequence</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 52.04%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 42K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 10m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Juggler Sequence is a series of integers in which the first term starts with a positive integer number <i>a</i> and the remaining terms are generated from the immediate previous term using the below recurrence relation:<br><br><img src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/705067/Web/Other/2220ffd2-353d-4b30-b2aa-68fe4047f959_1685087657.png" alt="Juggler Formula" title=""/><br><br>Given a number n, find the Juggler Sequence for this number as the first term of the sequence until it becomes 1.

<b>Examples:</b>

<pre><b>Input:</b> n = 9
<b>Output:</b> 9 27 140 11 36 6 2 1
<b>Explaination:</b> We start with 9 and use 
above formula to get next terms.</pre>

<pre><b>Input:</b> n = 6
<b>Output:</b> 6 2 1
<b>Explaination:</b> 
[6<sup>1/2</sup>] = 2. 
[2<sup>1/2</sup>] = 1.</pre>

<b>Constraints:</b><br>1 ≤ n ≤ 100

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Mathematical` `Recursion` `series` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Juggler Sequence](https://www.geeksforgeeks.org/juggler-sequence/)
