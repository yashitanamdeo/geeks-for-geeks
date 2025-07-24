<h1 align="center">Good Stones</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.74%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 21K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Geek is in a geekland which have a river and some stones in it. Initially geek can step on any stone. Each stone has a number on it representing the value of exact step geek can move. If the number is +ve then geeks can move right and if the number is -ve then geeks can move left. Bad Stones are defined as the stones in which if geeks steps, will reach a never ending loop whereas good stones are the stones which are safe from never ending loops. Return the number of <b>good stones</b> in river.

<b>Examples</b>

<pre><b>Input:</b> [2, 3, -1, 2, -2, 4, 1]
<b>Output: </b>3
<b>Explanation: </b>Index 3, 5 and 6 are safe only. As index 1, 4, 2 forms a cycle and from index 0 you can go to index 2 which is part of cycle.
 </pre>

<pre><b>Input:</b> [1, 0, -3, 0, -5, 0]
<b>Output:</b> 2
<b>Explanation: </b>Index 2 and 4 are safe only. As index 0, 1, 3, 5 form cycle.
  </pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function badStones() which takes integer <b>n</b> and an array <b>arr </b>as input, and return an interger value as the number of good stones. Here n is the lenght of arr.

<b>Expected Time Complexity</b> : O(N), N is the number of stones<br><b>Expected Auxiliary Space</b> : O(N), N is the number of stones

<br><b>Constraints:</b><br>   1 <= n < 10^5 (where n is the length of the array)<br>  -1000 <= arr[i] < 1000


<hr>

### Tags
- **Topic Tags:** `Greedy` `Dynamic Programming` `Graph`
- **Company Tags:** `None`
