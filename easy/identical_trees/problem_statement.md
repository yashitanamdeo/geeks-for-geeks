<h1 align="center">Identical Trees</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.01%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 289K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two binary trees with their root nodes <b>r1</b> and <b>r2</b>, return true if both of them are identical, otherwise, false.<br>

<b>Examples:</b>

<pre><b>Input:
</b>    1          1
   /   \       /   \
  2     3    2    3
<b>Output: </b>true<b>
Explanation: <br></b>There are two trees both having 3 nodes and 2 edges, both trees are identical having the root as 1, left child of 1 is 2 and right child of 1 is 3.</pre>

<pre><b>Input:
</b>    1         1
   /   \      /  \
  2     3   3   2
<b>Output: </b>false<b>
Explanation: </b>There are two trees both having 3 nodes and 2 edges, but both trees are not identical.</pre>

<pre><b>Input:
</b>    1   1
   /      \
  2        2
<b>Output: </b>false<b>
Explanation: </b>Although both trees have the same node values (1 and 2), they are arranged differently, making the trees non-identical.</pre>

<b>Constraints:</b><br>1 <= number of nodes <= 10<sup>5</sup><br>1 <= node->data <= 10<sup>9</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `Flipkart` `Amazon` `Microsoft`

### Related Articles
- [Write C Code To Determine If Two Trees Are Identical](https://www.geeksforgeeks.org/write-c-code-to-determine-if-two-trees-are-identical/)
