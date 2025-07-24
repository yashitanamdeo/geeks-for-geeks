<h1 align="center">Tree Transformation</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 54.63%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 23K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a tree containing <b>N</b> nodes in the form of an array <b>P</b> where <b>P<sub>i</sub></b> represents the parent of the <i>i-</i>th node and <b>P<sub>0</sub></b> = -1 as the tree is rooted at node 0. In one move, you can merge any two adjacent nodes. Calculate the minimum number of moves required to turn the tree into a <b>star</b> tree.


-> Merging adjacent nodes means deleting the edge between them and considering both the nodes as a single one.<br>-> A Star tree is a tree with a center node, and all other nodes are connected to the center node only.


<b>Example 1:</b>

<pre><b>Input:
</b>N = 5
p[] = {-1, 0, 0, 1, 1}
<b>Output:
</b>1
<b>Explanation</b>: 
Tree looks like:
            
Merge the node 2 to 0 in one operation

Our Tree will look like:
            
</pre>

<b>Example 2:</b>

<pre><b>Input:</b> N = 8
p[] = {-1 0 0 0 0 2 2 5}
<b>Output:</b>
2
<b>Explanation</b>:
Tree looks like:

        

Merge node 5 to 2, tree will look like

          

and then 2 to 0, finally the tree will be:

             

thus tree formed will be a star tree.
 
</pre>

<b>Your Task:</b><br>You don't need to read, input, or print anything. Your task is to complete the function <b><i>solve( )</i>, </b>which takes integer <b>N, </b>and an array <b>p[ ] </b>as input parameters and returns the minimum number of moves required to turn the tree into a <b>star</b> tree.

<b>Expected Time Complexity:</b> O(N)<br><b>Expected Auxiliary Space:</b> O(N)

<b>Constraints:</b><br>1 ≤ N ≤ 10<sup>5</sup><br>0 ≤ p[i] < N<br>p[0] = -1, 0 is the root node.


<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `None`
