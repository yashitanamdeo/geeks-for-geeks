<h1 align="center">Optimal binary search tree</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.02%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 11K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a sorted array <b>keys[0.. n-1]</b> of search keys and an array <b>freq[0.. n-1]</b> of frequency counts, where freq[i] is the number of searches to keys[i]. Construct a binary search tree of all keys such that the total cost of all the searches is as small as possible.<br>
Let us first define the cost of a BST. The cost of a BST node is level of that node multiplied by its frequency. Level of root is 1.

<br>
<b>Example 1:</b>

<pre><b>Input:</b>
n = 2
keys = {10, 12}
freq = {34, 50}
<b>Output:</b> 118
<b>Explaination:</b>
There can be following two possible BSTs 
        10                       12
          \                     / 
           12                 10
          <i>                    
The cost of tree I is 34*1 + 50*2 = 134
The cost of tree II is 50*1 + 34*2 = 118 </i></pre>

<br>
<i><b>Example 2:</b></i>

<pre><i>
<b>Input:</b>
N = 3
keys = {10, 12, 20}
freq = {34, 8, 50}
<b>Output:</b> 142
<b>Explaination:</b> There can be many possible BSTs
     20
    /
   10  
    \
     12  
     <i>
Among all possible BSTs, 
cost of this BST is minimum.  
Cost of this BST is 1*50 + 2*34 + 3*8 = 142</i></i></pre>

<br>
<i><i><b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>optimalSearchTree()</b> which takes the array <b>keys[], freq[]</b> and their size <b>n </b>as input parameters and returns the total cost of all the searches is as small as possible.</i></i>

<br>
<i><i><b>Expected Time Complexity:</b> O(n<sup>3</sup>)<br>
<b>Expected Auxiliary Space:</b> O(n<sup>2</sup>)</i></i>

<br>
<i><i><b>Constraints:</b><br>
1 ≤ N ≤ 100</i></i>


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Binary Search Tree` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Optimal Binary Search Tree Dp 24](https://www.geeksforgeeks.org/optimal-binary-search-tree-dp-24/)
