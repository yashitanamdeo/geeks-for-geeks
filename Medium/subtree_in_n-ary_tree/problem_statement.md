<h1 align="center">Subtree In N-ary Tree</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 77.56%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 17K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given the root of a n-ary tree find the number of duplicate subtrees in the n-ary tree. Two trees are <b>duplicates</b> if they have the <b>same structure</b> with the <b>same node values</b>.

<b>Examples:</b>

<pre><b>Input: </b>root = [1, N, 2, 2, 3, N, 4, N, 4, 4, 3, N, N N N N]
 <br><b>Output:</b> 2
<b>Explanation:</b> [4], [3] are duplicate subtree.
</pre>

<pre><b>Input: </b>root = [1, N, 2, 3, N, 4, 5, 6, N, N, N, N]
<br><b>Output: </b>0
<b>Explanation:</b> No duplicate subtree found.
</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function duplicateSubtreeNaryTree() which takes the root of the n-ary tree as input and returns an integer value as a number of duplicate subtrees.

<b>Expected Time Complexity:</b> O(n), n is the total no of nodes<br><b>Expected Space Complexity:</b> O(n<sup>2</sup>)

<b>Constraints:</b><br>   1 <= n < 10<sup>3</sup><br>   1 <= node.key< 10<sup>3</sup>


<hr>

### Tags
- **Topic Tags:** `Tree`
- **Company Tags:** `None`

### Related Articles
- [Count Of Duplicate Subtrees In An N Ary Tree](https://www.geeksforgeeks.org/count-of-duplicate-subtrees-in-an-n-ary-tree/)
