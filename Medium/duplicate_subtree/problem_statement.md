<h1 align="center">Duplicate Subtree</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 34.23%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 104K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary tree, find out whether it contains a duplicate sub-tree of size two or more, or not.

<b>Note:</b> Two same leaf nodes are not considered as subtree as size of a leaf node is one. <br><br><b>Example 1 :</b>

<pre><b>Input : </b>
               1
             /   \ 
           2       3
         /   \       \    
        4     5       2     
                     /  \    
                    4    5
<b>Output :</b> 1
<b>Explanation : </b>
    2     
  /   \    
 4     5
is the duplicate sub-tree.</pre>

<b>Example 2 :</b>

<pre><b>Input : </b>
               1
             /   \ 
           2       3
<b>Output: </b>0
<b>Explanation:</b> There is no duplicate sub-tree 
in the given binary tree.</pre>

<b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>dupSub()</b> which takes root of the tree as the only argument and returns 1 if the binary tree contains a duplicate sub-tree of size two or more, else 0.

<b>Expected Time Complexity:</b> O(N)<br><b>Expected Space Complexity:</b> O(N)

<b>Constraints:</b><br>0 ≤ Data of nodes ≤ 12<br>1 ≤ Number of nodes ≤ 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `Google`

### Related Articles
- [Check Binary Tree Contains Duplicate Subtrees Size 2](https://www.geeksforgeeks.org/check-binary-tree-contains-duplicate-subtrees-size-2/)
