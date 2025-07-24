<h1 align="center">Does array represent Heap</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 30.97%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 83K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr </b>of size <b>n</b>, the task is to check if the given array can be a level order representation of a [Max Heap](https://www.geeksforgeeks.org/difference-between-min-heap-and-max-heap/).

<b>Example 1:</b>

<pre><b>Input:<br></b>n = 6<br>arr[] = {90, 15, 10, 7, 12, 2}
<b>Output: <br></b>1<br><b>Explanation:</b> 
The given array represents below tree
       90
     /    \
   15      10
  /  \     /
7    12  2
The tree follows max-heap property as every
node is greater than all of its descendants.
</pre>

<b>Example 2:</b>
<pre><b>Input:  <br></b>n = 6<br>arr[] = {9, 15, 10, 7, 12, 11}
<b>Output:<br></b>0
<b>Explanation:</b><br>The given array represents below tree
       9
     /    \
   15      10
  /  \     /
7    12  11
The tree doesn't follows max-heap property 9 is
smaller than 15 and 10, and 10 is smaller than 11. </pre>

<b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>isMaxHeap()</b> which takes the array <b>arr[]</b> and its size <b>n</b><b> </b>as inputs and returns <b>True</b> if the given array could represent a valid level order representation of a <b>Max Heap</b>, or else, it will return <b>False</b>.

<b>Expected Time Complexity:</b> O(n)<br><b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>1 ≤ n ≤ 10<sup>5</sup><br>1 ≤ arr<sub>i</sub> ≤ 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Binary Search Tree` `Data Structures`
- **Company Tags:** `Cisco`

### Related Articles
- [How To Check If A Given Array Represents A Binary Heap](https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/)
