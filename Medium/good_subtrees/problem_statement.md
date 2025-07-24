<h1 align="center">Good Subtrees</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 69.2%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 19K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a <b>root</b> node of a binary Tree and each node of the binary tree is assigned a <b>value</b> and you are also given an integer <b>k</b> and you have to return the <b>count </b>of <b>Good subtrees</b> of this binary Tree . Good subtree is a subtree such that the <b>number</b> of <b>distinct</b> <b>values</b> in this subtree is less than or equal to k.

<b>Note</b>: Subtree of a node consists of that node and all nodes of the subtrees of left and right child  of that node  if they exist .

<b>Example 1:</b>

<pre><b>Input:</b>

<b>k=2</b>
<b>Output</b>: 4
<b>Explanation:</b>
We can see all leaves <b>3,4,5</b> form good subtrees as number of distinct values in subtrees is 1 which is less than k which is given as <b>2,</b>now  subtree which starts at 2 and has 3 as left node  is also a good subtree because the <b>count</b> of distinct values is <b>2</b> which is equal to k so overall 4 good subtrees.</pre>

<b>Example 2:</b>

<pre><b>Input:</b>

k=1
<b>Output: </b>4
<b>Explanation:</b>
we can see all leaves <b>2,2</b> form good subtrees as number of distinct values in subtrees is 1 which is equal to k which is given as 1, now  both subtrees which starts at 2 and has 2 as child also forms  a good subtree because <b>count</b> of distinct values is 1 which is equal to k so overall <b>4</b> good subtrees.</pre>

<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>goodSubtrees</b>() which takes <b>root</b> of binary tree  and an integer <b>k</b> respectively and you have to  return the <b>count</b> of good subtrees .

<b>Expected Time Complexity:</b> O(n*k)<br>
<b>Expected Space Complexity:</b> O(n+n*k), where n is the size of recursion stack.<br>
<br>
<b>Constraints</b>:<br>
1<=n<=10<sup>5</sup> (Number of nodes in binary Tree)<br>
1<=node.data<=25<br>
1<=k<=20<br>
The sum of n over all test cases won't exceed 5*10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `DFS` `Algorithms`
- **Company Tags:** `None`
