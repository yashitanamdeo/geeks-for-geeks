<h1 align="center">Find the string in grid</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 22.88%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 81K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a 2D grid of <b>n</b>*<b>m</b> of characters and a <b>word</b>, find all occurrences of given word in grid. A word can be matched in <b>all 8 directions</b> at any point. Word is said to be found in a direction if all characters match in this direction (not in zig-zag form). The 8 directions are, <b>horizontally left</b>, <b>horizontally right</b>, <b>vertically up</b>, <b>vertically down</b>, and <b>4 diagonal directions</b>.<br><br><b>Note:</b> The returning list should be <b>lexicographically smallest</b>. If the word can be found in multiple directions starting from the same coordinates, the list should contain the coordinates only once. 

<b>Example 1:</b>

<pre><b>Input: <br></b>grid = {{a,b,c},{d,r,f},{g,h,i}},
word = "abc"
<b>Output: <br></b>{{0,0}}
<b>Explanation: <br></b>From (0,0) we can find "abc" in horizontally right direction.
</pre>

<b>Example 2:</b>

<pre><b>Input: <br></b>grid = {{a,b,a,b},{a,b,e,b},{e,b,e,b}}
word = "abe"
<b>Output: <br></b>{{0,0},{0,2},{1,0}}
<b>Explanation: <br></b>From (0,0) we can find "abe" in right-down diagonal. <br>From (0,2) we can find "abe" in left-down diagonal. <br>From (1,0) we can find "abe" in horizontally right direction.
</pre>

<b>Your Task:</b><br>You don't need to read or print anything, Your task is to complete the function <b>searchWord() </b>which takes grid and word as input parameters and returns a list containing the positions from where the word originates in any direction. If there is no such position then returns an empty list.

<b>Expected Time Complexity: </b>O(n*m*k) where k is constant<br><b>Expected Space Complexity: </b>O(1)

<b>Constraints:</b><br>1 <= n <= m <= 50<br>1 <= |word| <= 15


<hr>

### Tags
- **Topic Tags:** `Recursion` `DFS` `Matrix` `Data Structures` `Algorithms`
- **Company Tags:** `Zoho` `Flipkart` `Amazon` `Microsoft` `Samsung` `FactSet`

### Related Articles
- [Search A Word In A 2d Grid Of Characters](https://www.geeksforgeeks.org/search-a-word-in-a-2d-grid-of-characters/)

### Related Interview Experiences
- [Samsung Bangalore Internship Interview Experience 2018](https://www.geeksforgeeks.org/samsung-bangalore-internship-interview-experience-2018/)
- [Samsung Research Institute Bangalore Srib Intern](https://www.geeksforgeeks.org/samsung-research-institute-bangalore-srib-intern/)
