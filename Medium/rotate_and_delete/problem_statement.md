<h1 align="center">Rotate and delete</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 20.63%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 58K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr</b> integers. Assume <b>sz </b>to be the initial size of the array. Do the following operations exactly <b>sz/2</b> times. In every <b>kth </b>(1<= k <= sz/2) operation:

- Right-rotate the array clockwise by <b>1</b>.
- Delete the<b> (n– k + 1)th </b>element from begin.
Now, Return the first element of the array.<br><b>Note:</b> Here n keeps on decreasing with every operation.

<b>Examples:</b>

<pre><b>Input: </b>arr<b> = </b>[1, 2, 3, 4, 5, 6]
<b>Output: </b>3
<b>Explanation: </b>Rotate the array clockwise i.e. after rotation the array arr = [6, 1, 2, 3, 4, 5] and delete the last element that is 5 that will be arr = [6, 1, 2, 3, 4]. Again rotate the array for the second time and deletes the second last element that is 2 that will be A = [4, 6, 1, 3], doing similar operation when we perform 4th operation, 4th last element does not exist. Then we deletes 1st element ie 1 that will be arr = [3, 6]. So, continuing this procedure the last element in arr is 2. So, the output will be 3.</pre>

<pre><b>Input: </b>arr<b> = </b>[1, 2, 3, 4]
<b>Output: </b>2
<b>Explanation:</b> Rotate the vector clockwise i.e. after rotation the vector arr = [4, 1, 2, 3] and delete the last element that is 3 that will be arr = [4, 1, 2]. After doing all the operations, the output will be 2.</pre>

<b>Expected Time Complexity:</b> O(n<sup>2</sup>)<br><b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>1 <= arr.size() <= 10<sup>3</sup><br>1 <= arr[i] <= 10<sup>6</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Find Last Element Of Array By Rotating And Deleting N K1 Element](https://www.geeksforgeeks.org/find-last-element-of-array-by-rotating-and-deleting-n-k1-element/)
