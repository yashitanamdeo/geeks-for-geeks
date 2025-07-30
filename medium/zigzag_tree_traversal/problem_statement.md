<h1 align="center">ZigZag Tree Traversal</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 54.05%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 178K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary tree with <b>n</b> nodes. Find the zig-zag level order traversal of the binary tree. <br>In zig zag traversal starting from the first level go from <b>left to right</b> for odd-numbered levels and <b>right to left </b>for even-numbered levels.

<b>Examples:</b>

<pre><b>Input:
</b>        1
      /   \
     2      3
    / \    /  \
   4   5  6    7
<b>Output: </b>[1, 3, 2, 4, 5, 6, 7]<br><b>Explanation:</b><br>For level 1 going left to right, we get traversal as {1}.<br>For level 2 going right to left, we get traversal as {3,2}.<br>For level 3 going left to right, we get traversal as {4,5,6,7}.<br>Merging all this traversals in single array we get {1,3,2,4,5,6,7}.
</pre>

<pre><b>Input:
</b>          7
        /   \
       9     7
     /  \   /   
    8   8  6     
   /  \
  10   9 
<b>Output: </b>[7, 7, 9, 8, 8, 6, 9, 10] <br><b>Explanation:<br></b>For level 1 going left to right, we get traversal as {7}.<br>For level 2 going right to left, we get traversal as {7,9}.<br>For level 3 going left to right, we get traversal as {8,8,6}.<br>For level 4 going right to left, we get traversal as {9,10}.<br>Merging all this traversals in single array we get {7,7,9,8,8,6,9,10}.<br></pre>

<pre><b>Input:
</b>          5
        /   \
       1     9
      / \   / \
     3   2 8   4

<b>Output: </b>[5, 9, 1, 3, 2, 8, 4]
<b>Explanation:<br></b>For level 1 going left to right, we get traversal as {5}.<br>For level 2 going right to left, we get traversal as {9,1}.<br>For level 3 going left to right, we get traversal as {3,2,8,4}.<br>Merging all this traversals in single array we get {5,9,1,3,2,8,4}.</pre>

<b><b>Constraints:</b></b><br>1 <= number of nodes <= 10<sup>5<br></sup>1 <= node->data <= 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Traversal` `Tree` `Data Structures` `Algorithms`
- **Company Tags:** `Flipkart` `Amazon` `Microsoft` `Snapdeal` `FactSet` `Hike` `Walmart` `Cisco`

### Related Interview Experiences
- [Flipkart Interview Experience Set 24](https://www.geeksforgeeks.org/flipkart-interview-experience-set-24/)
