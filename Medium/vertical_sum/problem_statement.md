<h1 align="center">Vertical sum</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 64.76%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 53K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary tree having <b>n</b> nodes, find the vertical sum of the nodes that are in the same vertical line. Return all sums through different vertical lines starting from the left-most vertical line to the right-most vertical line.

<b>Example 1:</b>

<pre><b>Input:</b>
       1
    /  \
  2     3
 / \   / \
4   5 6   7
<b>Output: <br></b>4 2 12 3 7<b>
Explanation:</b>
The tree has 5 vertical lines
Line 1 has only one node 4 => vertical sum is 4.
Line 2 has only one node 2 => vertical sum is 2.
Line-3 has three nodes: 1,5,6 => vertical sum is 1+5+6 = 12.
Line-4 has only one node 3 => vertical sum is 3.
Line-5 has only one node 7 => vertical sum is 7.
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
          1<br>         /<br>        2<br>       /<br>      3<br>     /<br>    4<br>   /<br>  6<br> /<br>7
<b>Output: <br></b>7 6 4 3 2 1<b>
Explanation:</b>
There are six vertical lines each having one node.</pre>

<b>Your Task:</b><br>You don't need to take input. Just complete the function<b> verticalSum() </b>that takes <b>root </b>node of the tree<b> </b>as parameter and returns an array containing the vertical sum of tree from left to right.

<b>Expected Time Complexity</b>: O(nlogn).<br><b>Expected Auxiliary Space: </b>O(n).

<b>Constraints:</b><br>1<=n<=10<sup>4</sup><br>1<= Node value <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `Amazon`

### Related Articles
- [Vertical Sum In A Given Binary Tree](https://www.geeksforgeeks.org/vertical-sum-in-a-given-binary-tree/)

### Related Interview Experiences
- [Amazon Interview Experience Set 255 On Campus](https://www.geeksforgeeks.org/amazon-interview-experience-set-255-on-campus/)
- [Amazon Interview Set 86 Sde](https://www.geeksforgeeks.org/amazon-interview-set-86-sde/)
- [Amazon Interview Experience Set 273 On Campus](https://www.geeksforgeeks.org/amazon-interview-experience-set-273-on-campus/)
