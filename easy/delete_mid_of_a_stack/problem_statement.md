<h1 align="center">Delete Mid of a Stack</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.71%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 158K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a stack <b>s</b>, delete the <b>middle element </b>of the stack without using any additional data structure.


<b>Middle element:- </b>floor((size_of_stack+1)/2) (1-based indexing) from the bottom of the stack.


Note: The output shown by the compiler is the stack from top to bottom.

<b>Examples:</b>

<pre><b>Input</b>: s = [10, 20, 30, 40, 50]
<b>Output</b>: [50, 40, 20, 10]
<b>Explanation</b>: The bottom-most element will be 10 and the top-most element will be 50. Middle element will be element at index 3 from bottom, which is 30. Deleting 30, stack will look like {10 20 40 50}.
</pre>

<pre><b>Input</b>: s = [10, 20, 30, 40]
<b>Output</b>: [40, 30, 10]
<b>Explanation</b>: The bottom-most element will be 10 and the top-most element will be 40. Middle element will be element at index 2 from bottom, which is 20. Deleting 20, stack will look like {10 30 40}.<br></pre>

<pre><b>Input</b>: s = [5, 8, 6, 7, 6, 6, 5, 10, 12, 9]
<b>Output</b>: [9, 12, 10, 5, 6, 7, 6, 8, 5]</pre>

<b>Constraints:</b><br>2 ≤ element of stack ≤ 10<sup>5<br></sup>2 ≤ s.size() ≤ 10<sup>4</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Recursion` `Stack` `STL` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon`

### Related Articles
- [Delete Middle Element Stack](https://www.geeksforgeeks.org/delete-middle-element-stack/)
- [Design A Stack With Find Middle Operation](https://www.geeksforgeeks.org/design-a-stack-with-find-middle-operation/)
