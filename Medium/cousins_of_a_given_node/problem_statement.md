<h1 align="center">Cousins of a given node</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 49.75%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 14K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary tree and a node, print all cousins of given node in order of their appearance. Note that siblings should not be printed.

<b>Example 1:</b>

<pre><b>Input : </b>
             1
           /   \
          2     3
        /   \  /  \
       4    5  6   7

Given node : 5
<b>Output :</b> 6 7
<b>Explanation :</b>
Nodes 6 and 7 are on the same level 
as 5 and have different parents.

</pre>

<b>Example 2 :</b>

<pre><b>Input :
</b>         9
        /
       5
Given node : 5
<b>Output :</b> -1
<b>Explanation :</b>
There no other nodes than 5 in the same level.
</pre>

<b>Your task :</b>
You don't have to read input or print anything. Your task is to complete the function<b> printCousins() </b>which takes the root node of the tree and the node whose cousins need to be found, as input and returns a list containing the cousins of the given node in order of their appearance in the tree. If there is no cousin of the given node, return<b> -1</b> as the first element of the list.
 
<b>Expected Time Complexity : </b>O(n)
<b>Expected Auxiliary Space : </b>O(n)
 
<b>Constraints :</b>
1 <= n <=10^5


<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `Microsoft`

### Related Articles
- [Print Cousins Of A Given Node In Binary Tree Single Traversal](https://www.geeksforgeeks.org/print-cousins-of-a-given-node-in-binary-tree-single-traversal/)
