<h1 align="center">Previous number in one swap</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 30.54%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 12K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a non-negative number N in the form of string. The task is to apply at most one swap operation on the number N so that the result is just a previous possible number.

<b>Note:  </b>Leading zeros are not allowed.

 

Example 1:

<pre><b>Input :
</b>S = "12435"
<b>Output: 
</b>12345
<b>Explanation:
</b>Although the number 12354 
will be the largest smaller 
number from 12435. But it is 
not possible to make it using 
only one swap. So swap 
4 and 3 and get 12345.</pre>

 

Example 2:

<pre><b>Input: 
</b>S = " 12345"
<b>Output: 
</b>-1
<b>Explanation:
</b>Digits are in increasing order. 
So it is not possible to 
make a smaller number from it.</pre>

 

<b>Your Task:</b>

You don't need to read input or print anything. Your task is to complete the function previousNumber() which takes the string S and returns the previous number of S. If no such number exists return -1;

 

Expected Time Complexity: O(N)<br>
Expected Auxiliary Space: O(1)

 

<b>Constraints:</b><br>
2<=|Number length |<=10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Strings` `Numbers` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Largest Number With One Swap Allowed](https://www.geeksforgeeks.org/largest-number-with-one-swap-allowed/)
