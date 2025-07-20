<h1 align="center">Iterative Postorder</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 80.67%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 47K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary tree. Find the postorder traversal of the tree <b>without using recursion</b>. Return a list containing the postorder traversal of the tree, calculated<b> without using recursion.</b>

<b>Examples :</b>

<pre><b>Input:</b>
<b>           </b>1
<b>         /   \</b>
        2     3
      /  \
     4    5

<b>Output: </b>4 5 2 3 1
<b>Explanation: </b>Postorder traversal (Left->Right->Root) of the tree is 4 5 2 3 1.
</pre>

<pre><b>Input:</b>
             8
          /      \
        1          5
         \       /   \
          7     10    6
           \   /
            10 6

<b>Output: </b>10 7 1 6 10 6 5 8 
<b>Explanation: </b>Postorder traversal (Left->Right->Root) of the tree is 10 7 1 6 10 6 5 8 .</pre>

 
<b>Expected time complexity: </b>O(n)
<b>Expected auxiliary space: </b>O(n)
 
<b>Constraints:</b>
1 <= Number of nodes <= 10<sup>5</sup><br>1 <= Data of a node <= 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Stack` `Tree` `Data Structures`
- **Company Tags:** `Microsoft`

### Related Articles
- [Iterative Postorder Traversal Using Stack](https://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/)
