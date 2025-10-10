<h1 align="center">ZigZag Tree Traversal</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 54.05%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 186K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given the <b>root </b>of a binary tree. You have to find the <b>zig-zag </b>level order traversal of the binary tree. <br><b>Note: </b>In zig zag traversal we traverse the nodes from <b>left to right </b>for odd-numbered levels, and from <b>right to left</b> for even-numbered levels.

<b>Examples:</b>

<pre><b>Input: </b>root = [1, 2, 3, 4, 5, 6, 7]<b><br> </b><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/907336/Web/Other/blobid0_1754394121.webp" alt="" title="" width="274" height="190"/><b> </b>        
<b>Output: </b>[1, 3, 2, 4, 5, 6, 7]<br><b>Explanation:<br></b>Level 1 (left to right): [1]<br>Level 2 (right to left): [3, 2]<br>Level 3 (left to right): [4, 5, 6, 7]<br>Final result: [1, 3, 2, 4, 5, 6, 7]</pre>

<pre><b>Input: </b>root = [7, 9, 7, 8, 8, 6, N, 10, 9]<br><b><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/907336/Web/Other/blobid2_1754394198.webp" alt="" title="" width="287" height="252"/> </b>
<b>Output: </b>[7, 7, 9, 8, 8, 6, 9, 10] <br><b>Explanation:<br></b>Level 1 (left to right): [7]<br>Level 2 (right to left): [7, 9]<br>Level 3 (left to right): [8, 8, 6]<br>Level 4 (right to left): [9, 10]<br>Final result: [7, 7, 9, 8, 8, 6, 9, 10]</pre>

<b><b>Constraints:</b></b><br>1 ≤ number of nodes ≤ 10<sup>5<br></sup>1 ≤ node->data ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Traversal` `Tree` `Data Structures` `Algorithms`
- **Company Tags:** `Flipkart` `Amazon` `Microsoft` `Snapdeal` `FactSet` `Hike` `Walmart` `Cisco`

### Related Interview Experiences
- [Flipkart Interview Experience Set 24](https://www.geeksforgeeks.org/flipkart-interview-experience-set-24/)
