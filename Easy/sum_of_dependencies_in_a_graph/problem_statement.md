<h1 align="center">Sum of dependencies in a graph</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 66.93%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 50K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a directed graph with <b>V</b> nodes and <b>E</b> edges, the graph's edges are represented as a 2D array, <b>edges</b>[][]. Each row in the array represents a directed edge (<b>u</b>, <b>v</b>), meaning there is a directed edge from node <b>u</b> to node <b>v</b>. If there is a directed edge from <b>u</b> to<b> </b><b>v</b>, it means that <b>u</b> depends on <b>v</b>. The Number of Dependencies (NoD) for a node <b>x</b> is the total count of nodes that <b>x</b> depends upon.

Your task is to calculate the sum of the Number of Dependencies (NoD) for all nodes in the graph.

<b>Examples:</b>

<pre><b>Input:</b> V<b> </b>= 4, E<b> </b>= 4, edges[][] = [[0,2],[0,3],[1,3],[2,3]]

<b>Output: </b>4
<b>Explanation: </b>For the graph in diagram, A depends on C and D i.e. A's NoD is 2, B depends on D i.e. B's NoD is 1, C depends on D i.e. D's NoD is 1 and D depends on none. Hence answer is 2 + 1 + 1 + 0 = 4.</pre>

<pre><b>Input:</b> V<b> </b>= 4, E<b> </b>= 3, edges[][]<b> </b>= [[0,3],[0,2],[0,1]]
<b>Output: </b>3
<b>Explanation: </b>The sum of dependencies: 3 + 0 + 0 + 0 = 3.</pre>

<b>Constraints:</b><br>1 <= V <= 10<sup>5<br></sup>1 <= E <= 10<sup>5<br></sup>edges.size() = E<br>edges[i].size() = 2<br>0 <= edges[i][j] <= V-1

## Expected Complexities
- Time Complexity: O(1)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Graph` `Data Structures`
- **Company Tags:** `Flipkart`

### Related Articles
- [Sum Dependencies Graph](https://www.geeksforgeeks.org/sum-dependencies-graph/)

### Related Interview Experiences
- [Flipkart Interview Set 11](https://www.geeksforgeeks.org/flipkart-interview-set-11/)
