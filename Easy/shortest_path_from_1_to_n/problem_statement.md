<h1 align="center">Shortest path from 1 to n</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 37.62%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 85K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 10m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Consider a <b>directed graph </b>whose vertices are numbered from <b>1</b> <b>to n</b>. There is an edge from a vertex <b>i</b> to a vertex <b>j</b> if and only if either <b>j = i + 1 or j = 3 * i</b>. The task is to find the <b>minimum </b>number of edges in a path from vertex <b>1</b> to vertex <b>n</b>.

<b>Examples :</b>

<pre><b>Input: </b>n = 9
<b>Output: </b>2
<b>Explanation</b>: Many paths are possible from 1 to 9. Shortest one possible is, 1 -> 3 -> 9, of length 2.</pre>

<pre><b>Input</b>: n = 4
<b>Output: </b>2
<b>Explanation</b>: Possible paths from 1 to 4 are, 1 -> 2 -> 3 -> 4 and 1 -> 3 -> 4. Second path of length 2 is the shortest.<br></pre>

<pre><b>Input</b>: n = 15
<b>Output: </b>4</pre>

<b>Constraints:</b><br>1 ≤ n ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(log n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Mathematical` `Graph` `Shortest Path` `Data Structures` `Algorithms`
- **Company Tags:** `Morgan Stanley` `Accolite` `Samsung` `Synopsys` `Cisco`
