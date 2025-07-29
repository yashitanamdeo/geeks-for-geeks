<h1 align="center">Array Operations</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.0%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 35K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array <b>arr</b> of <b>n </b>integers. You must return the minimum number of operations required to make this array 0. For this you can do an operation :

- Choose a sub-array of non-zero elements & replace all with 0(0 must be present in arr, if not you can not replace it).
<b>Examples<br></b>

<pre><b>Input: </b>n = 4 arr = {3,0,4,5} <br><b>Output: </b>2
<b>Explanation: </b>First, we can choose 3 replace with 0(which is on 1st Index) and in the second operation, we can choose 4 & 5 -> replace with 0(1st Index).</pre>

<pre><b>Input</b>: n = 8 arr = {10,4,9,6,10,10,4,4} <br><b>Output: </b>-1 <br><b>Explanation</b>: If we do operations here, we can not make the entire 0 because no 0 is present in the array, hence -1.</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>arrayOperations()</b> which takes an integer <b>n</b> and an array <b>arr</b> as inputs and find the <b>minimum</b> number of operations you must perform to make all the elements of the array <b>0</b>. If not possible <b>return -1</b>;

<b>Expected Time Complexity:</b> O(N)<br><b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>1 <= n <= 10<sup>5</sup><br>0 <= arr[i] <= 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Mathematical` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Minimum Operations To Make All Array Elements 0 By Mex Replacement](https://www.geeksforgeeks.org/minimum-operations-to-make-all-array-elements-0-by-mex-replacement/)
