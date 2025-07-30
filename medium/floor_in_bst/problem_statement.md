<h1 align="center">Floor in BST</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.06%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 114K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a BST(Binary Search Tree) with <b>n</b> number of nodes and value <b>x</b>. your task is to find the greatest value node of the BST which is smaller than or equal to x.<br><b>Note:</b> when x is smaller than the smallest node of BST then returns -1.

<b>Examples:</b>

<pre><b>Input:</b>
n = 7               2
                     \
                      81
                    /     \
                 42       87
                   \       \
                    66      90
                   /
                 45
x = 87
<b>Output: </b>87
<b>Explanation: </b>87 is present in tree so floor will be 87.
</pre>

<pre><b>Input:</b>
n = 4                     6
                           \
                            8
                          /   \
                        7       9
x = 11
<b>Output: </b>9
</pre>

<pre><b>Input:</b>
n = 4                     6
                           \
                            8
                          /   \
                        7       9
x = 5
<b>Output: </b>-1<br></pre>

<b>Constraint:</b><br>1 <= Noda data <= 10<sup>9</sup><br>1 <= n <= 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(height of tree)
- Auxiliary Space: O(height of tree)

<hr>

### Tags
- **Topic Tags:** `Binary Search Tree` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Floor In Binary Search Tree Bst](https://www.geeksforgeeks.org/floor-in-binary-search-tree-bst/)
