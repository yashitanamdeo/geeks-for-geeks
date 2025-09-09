<h1 align="center">Assign Mice Holes</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 55.93%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 21K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given two arrays <b>mices[]</b> and <b>holes[]</b> of the same size. The array <b>mices[]</b> represents the positions of the mice on a straight line, while the array <b>holes[]</b> represents the positions of the holes on the same line. Each hole can accommodate exactly one mouse. A mouse can either stay in its current position, move one step to the right, or move one step to the left, and each move takes <b>one</b> minute. The task is to assign each mouse to a distinct hole in such a way that the time taken by the last mouse to reach its hole is <b>minimized</b>.

<b>Examples:</b>

<pre><b>Input:</b> mices[] = [4, -4, 2], holes[] = [4, 0, 5] <br><b>Output: </b>4
<b>Explanation: </b>Assign the mouse at position 4 to the hole at position 4, so the time taken is 0 minutes. Assign the mouse at position −4 to the hole at position 0, so the time taken is 4 minutes. Assign the mouse at position 2 to the hole at position 5, so the time taken is 3 minutes. Hence, the maximum time required by any mouse is 4 minutes.</pre>

<pre><b>Input:</b> mices[] = [1, 2], holes[] = [20, 10] <br><b>Output: </b>18 <br><b>Explanation: </b>Assign the mouse at position 1 to the hole at position 10, so the time taken is 9 minutes. Assign the mouse at position 2 to the hole at position 20, so the time taken is 18 minutes. Hence, the maximum time required by any mouse is 18 minutes.</pre>

<b>Constraints:</b><br>1 ≤ mices.size() = holes.size() ≤ 10<sup>5</sup><br>-10<sup>5 </sup>≤ mices[i] , holes[i] ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n log n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Mathematical` `Algorithms` `Greedy` `Sorting`
- **Company Tags:** `None`

### Related Articles
- [Assign Mice Holes](https://www.geeksforgeeks.org/assign-mice-holes/)
