<h1 align="center">Find the Maximum Flow</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 44.73%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 10K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a graph which represents a flow network with N vertices numbered 1 to N and M edges.Find the maximum flow from vertex numbered 1 to vertex numbered N.

In a flow network,every edge has a flow capacity and the maximum flow of a path can't exceed the flow-capacity of an edge in the path.<br>
<br>
<b>Example 1:</b>

<pre><b>Input:</b>
N = 5, M =  4
Edges[]= {{1,2,1},{3,2,2},{4,2,3},{2,5,5}}
<b>Output: </b>1 
<b>Explanation: </b>
1 - 2 - 3
   / \
  4   5 
1 unit can flow from 1 -> 2 - >5 
</pre>

 

<b>Example 2:</b>

<pre><b>Input:</b>
N = 4, M = 4
Edges[] = {{1,2,8},{1,3,10},{4,2,2},{3,4,3}}
<b>Output: </b>5 
<b>Explanation:</b>
  1 - 2 
  |   |
  3 - 4
3 unit can flow from 1 -> 3 -> 4
2 unit can flow from 1 -> 2 -> 4
Total max flow from 1 to N = 3+2=5</pre>

<b>Your Task: </b><br>
You don't need to read input or print anything. Your task is to complete the function<b> solve()</b> which takes the <b>N </b>(the number of vertices) ,<b>M </b>(the number of Edges) and the array <b>Edges</b>[] (Where Edges[i] denoting an undirected edge between Edges[i][0] and Edges[i][1] with a flow capacity of Edges[i][2]), and returns the integer denoting the maximum flow from 1 to N.

<b>Expected Time Complexity:</b> O(max_flow*M)<br>
<b>Expected Auxiliary Space:</b> O(N+M)

Where max_flow is the maximum flow from 1 to N

<b>Constraints:</b><br>
1 <= N,M,Edges[i][2] <= 1000<br>
1 <= Edges[i][0],Edges[i][1] <= N


<hr>

### Tags
- **Topic Tags:** `Graph` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Ford Fulkerson Algorithm For Maximum Flow Problem](https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/)
