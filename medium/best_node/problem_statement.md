<h1 align="center">Best Node</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 64.05%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 16K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a tree rooted at node <b>1</b>. The tree is given in form of an array <b>P</b> where <b>P<sub>i</sub></b> denotes the parent of node <b>i</b>, Also <b>P<sub>1</sub></b> = <b>-1</b>, as node 1 is the root node. Every node <b>i</b> has a value <b>A<sub>i</sub></b> associated with it. At first, you have to choose any node to start with, after that from a node you can go to any of its child nodes. You've to keep moving to a child node until you reach a leaf node. Every time you get to a new node, you write its value. Let us assume that the integer sequence in your path is <b>B</b>.<br>
Let us define a function <i>f</i> over <b>B</b>, which is defined as follows:<br>
<i>f(B) = </i>B<sub>1</sub> - B<sub>2</sub> + B<sub>3</sub> - B<sub>4</sub> + B<sub>5</sub>.... + (-1)<sup>(k-1)</sup>B<sub>k</sub>.<br>
You have to find the maximum possible value of <i>f(B)</i>.

<b>Example 1:</b>

<pre><b>Input:</b>
N = 3,
A = { 1, 2, 3}
P = {-1, 1, 1}
Output:
3
Explanation:
The resulting tree is:
        1(1)
      /     \
     2(2)   3(3)
If we choose our starting node as 3, then the
resulting sequence will be B = { 3 },
which will give the maximum possible value.</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>N = 3,
A = { 3, 1, 2}
P = {-1, 1, 2}
<b>Output:
</b>4<b>
Explanation:
</b>The resulting tree is:
  1(3)
  |
  2(1)
  |
  3(2)
If we choose our starting node as 1, then the
resulting sequence will be B = { 3 , 1 , 2 }.
The value which we'll get is, 3-1+2 = 4, which
is the maximum possible value.</pre>

<b>Your Task:</b><br>
The task is to complete the function <b>bestNode()</b> which takes an integer <b>N</b> and two integer arrays <b>A</b>, <b>P</b> as input parameters and returns the maximum possible value possible.

<b>Expected Time Complexity: O(N)<br>
Expected Space Complexity: O(N)</b>

<b>Constraints:</b><br>
1 ≤  N ≤ 10<sup>5</sup><br>
-10<sup>5</sup> ≤  A<sub>i</sub> ≤ 10<sup>5</sup><br>
-1 ≤  P<sub>i</sub> ≤ N


<hr>

### Tags
- **Topic Tags:** `Tree` `DFS`
- **Company Tags:** `None`

### Related Articles
- [Find The Maximum Possible Value Of Fb](https://www.geeksforgeeks.org/find-the-maximum-possible-value-of-fb/)
