<h1 align="center">Find kth element of spiral matrix</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.66%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 53K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a matrix with <b>n</b> rows and <b>m </b>columns. Your task is to find the <b>kth</b> element which is obtained while traversing the matrix spirally. You need to complete the method<b> findK</b> which takes four arguments the first argument is the matrix <b>A </b>and the next two arguments will be <b>n </b>and <b>m </b>denoting the size of the matrix A and then the forth argument is an integer <b>k</b>. The function will return the kth element obtained while traversing the matrix spirally.

<b>Example 1</b><b>:</b>

<pre><b>Input:
</b>n = 4, m = 4, k = 10
A[][] = {{1  2  3  4},
         {5  6  7  8},
         {9  10 11 12},<br>         {13 14 15 16}}
<b>Output:
</b>13<b>
Explanation:<br></b>
The spiral order of matrix will look like 1->2->3->4->8->12->16->15->14->13->9->5->6->7->11->10. So the 10th element in this order is 13. </pre>

<b>Example 2</b><b>:</b>

<pre><b>Input:
</b>n = 3, m = 3, k = 4
A[][] = {{1 2 3},
         {4 5 6},
         {7 8 9}}
<b>Output:
</b>6<b>
Explanation:</b>
The spiral order of matrix will look like 1->2->3->6->9->8->7->4->5. So the 4th element in this order is 6.</pre>

<b>Your Task:</b><br>You only need to implement the given function <b>findK()</b>. Do not read input, instead use the arguments given in the function. Return the K'th element obtained by traversing matrix spirally.

<b>Expected Time Complexity:</b> O(n*m)<br><b>Expected Auxiliary Space:</b> O(n*m)

<b>Constraints:</b><br>1<=n,m<=10<sup>3</sup><br>1<=k<=n*m<br>-10<sup>9</sup> <= A[i][j] <= 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Matrix` `Data Structures`
- **Company Tags:** `Amazon` `Bloomberg` `Facebook` `Microsoft` `Uber`

### Related Articles
- [Print Kth Element Spiral Form Matrix](https://www.geeksforgeeks.org/print-kth-element-spiral-form-matrix/)
