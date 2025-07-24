<h1 align="center">Shortest Path Using Atmost One Curved Edge</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 59.43%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 18K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an undirected, connected graph with <b>n</b> vertices and <b>m</b> double-edges stored in <b>edges[][]</b> 2-D array. Each double-edge is represented by a tuple <b>(x, y, w1, w2)</b>, which indicates that there are two edges between vertices <b>x</b> and <b>y</b>: a straight edge with weight <b>w1</b> and a curved edge with weight <b>w2</b>.

You are given two vertices <b>a</b> and <b>b</b> and you have to go from <b>a</b> to <b>b</b> through a series of edges such that in the entire path, you can use at most 1 curved edge. Your task is to find the shortest path from <b>a</b> to <b>b</b> satisfying the above condition.

<b>Examples</b>

<pre><b>Input: </b>n = 4, m = 4, a = 2, b = 4, edges[][] = [[1, 2, 1, 4], [1, 3, 2, 4],[1, 4, 3, 1], [2, 4, 6, 5]]
<b>Output: </b>2
<br><b>Explanation:</b>
We can follow the path 2 -> 1 -> 4. This gives a distance of 1+3 = 4 if we follow all straight paths. But we can take the curved path  from 1 -> 4, which costs 1. This will result in a cost of 1 + 1 = 2
</pre>

<pre><b>Input: </b>n = 2, m = 1, a = 1, b = 2, edges = [[1, 2, 4, 1]]
<b>Output : </b>1

<b>Explanation:</b>
Take the curved path from 1 to 2 which costs 1. 
</pre>

<br><b>Constraints:</b>

- 1 ≤ n ≤ 10<sup>5</sup>
- 1 ≤ m ≤ 2 x 10<sup>5</sup>
- 1 ≤ a, b ≤ n
- 1 ≤ edges[i][0], edges[i][1] ≤ n
- 0 ≤ edges[i][2], edges[i][3] ≤ 10<sup>4</sup>

## Expected Complexities
- Time Complexity: O((m+n)log(n))
- Auxiliary Space: O(n+m)

<hr>

### Tags
- **Topic Tags:** `Graph` `Shortest Path` `Data Structures` `Algorithms`
- **Company Tags:** `Uber`

### Related Articles
- [Shortest Path With One Curved Edge In An Undirected Graph](https://www.geeksforgeeks.org/shortest-path-with-one-curved-edge-in-an-undirected-graph/)

### Related Interview Experiences
- [Uber Interview Experience On Campus For Internship 2018 19](https://www.geeksforgeeks.org/uber-interview-experience-on-campus-for-internship-2018-19/)
