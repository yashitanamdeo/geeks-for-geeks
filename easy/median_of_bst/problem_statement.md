<h1 align="center">Median of BST</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 27.43%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 97K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a Binary Search Tree, find the Median of its Node values.

<b>Examples:</b>

<pre><b>Input: </b>root = [6, 3, 8, 1, 4, 7, 9]
       6
     /   \
   3      8   
 /  \    /  \
1    4  7    9<b>
Output: </b>6
<b>Explanation: </b>Inorder of Given BST will be: 1, 3, 4, 6, 7, 8, 9. So, here median will 6.
</pre>

<pre><b>Input: </b>root = [6, 3, 8, 1, 4, 7, N]
       6
     /   \
   3      8   
 /   \    /   
1    4   7   <b>
Output: </b>5<b>
Explanation:</b>Inorder of Given BST will be: 1, 3, 4, 6, 7, 8. So, here median will (4 + 6)/2 = 10/2 = 5.<br></pre>

<pre><b>Input: </b>root = [18, 16, 20, 7]<b>
Output: </b>17</pre>

<b>Constraints:</b><br>1<=n<=10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(Height of the BST)

<hr>

### Tags
- **Topic Tags:** `Traversal` `Binary Search Tree` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon`

### Related Articles
- [Find Median Bst Time O1 Space](https://www.geeksforgeeks.org/find-median-bst-time-o1-space/)
