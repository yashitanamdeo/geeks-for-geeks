<h1 align="center">Find Common Nodes in two BSTs</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.7%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 71K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two Binary Search Trees. Find the nodes that are common in both of them, ie- find the intersection of the two BSTs.

<b>Note</b>: Return the common nodes in <b>sorted </b>order.

<b>Examples:</b>

<pre><b>Input:
</b><b>BST1:
</b>                  5
               /     \
             1        10
           /   \      /
          0     4    7
                      \
                       9
<b>BST2:
</b>                10 
              /    \
             7     20
           /   \ 
          4     9
<b><br>Output: </b>4 7 9 10

</pre>

<pre><b>Input:
BST1:
</b>     10
    /  \
   2   11
  /  \
 1   3
<b>BST2:
</b>       2
     /  \
    1    3
<b>Output: </b>1 2 3
</pre>

<b>Constraints:</b><br>1 <= Number of Nodes <= 10<sup>5</sup><br>1 <= Node data <= 10<sup>9</sup>

## Expected Complexities
- Time Complexity: O(N1 + N2)
- Auxiliary Space: O(H1 + H2)

<hr>

### Tags
- **Topic Tags:** `Binary Search Tree` `Tree` `Data Structures`
- **Company Tags:** `Amazon`

### Related Articles
- [Print Common Nodes In Two Binary Search Trees](https://www.geeksforgeeks.org/print-common-nodes-in-two-binary-search-trees/)
