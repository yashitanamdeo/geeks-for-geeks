<h1 align="center">Count Full Binary Trees</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.61%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 14K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[]</b> of <b>n</b> integers, where each integer is greater than 1. The task is to find the number of [Full binary tree](http://quiz.geeksforgeeks.org/binary-tree-set-3-types-of-binary-tree/) from the given integers, such that each non-leaf node value is the product of its children value.<br><br><b>Note:</b> Each integer can be used multiple times in a full binary tree. The answer can be large, return  answer modulo 1000000007<br><br><b>Example 1:</b>
<pre><b>Input:</b>
n = 4
arr[] = {2, 3, 4, 6}
<b>Output:
</b>7
<b>Explanation:</b>
There are 7 full binary tree with
the given product property.
Four trees with single nodes
2  3  4  6
Three trees with three nodes
    4   
   / \
  2   2 ,
   6    
  / \
 2   3 ,
   6
  / \
 3   2</pre>

 

<b>Example 2:</b>
<pre>Input: 
n = 3
arr[] = {2, 4, 5} 
<b>Output: </b>4
<b>Explanation:</b> There are 4 full binary tree
with the given product property. 
Three trees with single nodes 2 4 5
One tree with three nodes
   4
  / \
 2  2</pre>

 

<b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>numoffbt()</b> which takes the array <b>arr[]</b>and its size <b>n</b><b> </b>as inputs and returns the number of Full binary tree.<br><br><b>Expected Time Complexity:</b> O(n. Log(n))<br><b>Expected Auxiliary Space:</b> O(n)<br><br><b>Constraints:</b><br>1 ≤ n ≤ 10<sup>5</sup><br>2 ≤ arr[i] ≤ 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Tree` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Number Full Binary Trees Node Product Children](https://www.geeksforgeeks.org/number-full-binary-trees-node-product-children/)
