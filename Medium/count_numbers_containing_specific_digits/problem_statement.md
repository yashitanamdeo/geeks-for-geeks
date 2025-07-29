<h1 align="center">Count Numbers Containing Specific Digits</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 57.08%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 14K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 25m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an integer <b>n</b> representing the number of digits in a number, and an array arr[] containing digits from 0 to 9. You have to count how many <b>n-digit</b> positive integers can be formed such that <b>at least</b> one digit from the array arr<b>[]</b> appears in the number.<br>

<b>Examples:<br></b>

<pre><b>Input: </b>n = 1, arr[] = [1, 2, 3]<b><br>Output: </b>3<b><br>Explanation: </b>Only the single-digit numbers [1, 2, 3] satisfy the condition.</pre>

<pre><b>Input: </b>n = 2, arr[] = [3, 5]<b><br>Output: </b>34<b><br>Explanation: </b>There are a total of 34  two digit numbers which contain atleast  one out of  [3, 5].<br></pre>

<b>Constraints:<br></b>  1 ≤ n ≤ 9<br>  1 ≤ arr.size() ≤ 10<br>  0 ≤ arr[i] ≤ 9

## Expected Complexities
- Time Complexity: O(log n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Mathematical`
- **Company Tags:** `None`

### Related Articles
- [Must Have Digit](https://www.geeksforgeeks.org/must-have-digit/)
