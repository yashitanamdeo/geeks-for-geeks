<h1 align="center">Last Moment Before All Ants Fall Out</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 62.2%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 13K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

We have a wooden plank of length <b>n</b> units. Some ants are walking on the plank, each ant moves with a speed of <b>1</b> unit per second, with some moving left and others right.<br>When two ants moving in two different directions meet at <b>some point</b>, they <b>change their directions</b> and continue moving again. Assume changing directions does not take any additional time. When an ant reaches one end of the plank at a time <b>t</b>, it falls out of the plank immediately.

Given an integer <b>n</b> and two integer arrays <b>left[]</b> and <b>right[]</b>, the positions of the ants moving to the left and the right, return the <b>time</b> when the last ant(s) fall out of the plank.

<b>Examples :</b>

<pre><b>Input: </b>n = 4, left[] = [2], right[] = [0, 1, 3]<br><b>Output:</b> 4<br>        <br><b>Explanation: </b>As seen in the above image, the last ant falls off the plank at t = 4.</pre>

<pre><b>Input:</b>  n = 4, left[] = [], right[] = [0, 1, 2, 3, 4]
<b>Output: </b>4<b><br></b>        <br><b>Explanation:</b> All ants are going to the right, the ant at index 0 needs 4 seconds to fall.<br></pre>

<pre><b>Input:</b> n = 3, left[] = [0], right[] = [3]
<b>Output:</b> 0<br><b>Explanation:</b> The ants will fall off the plank as they are already on the end of the plank.</pre>

<b>Constraints:<br></b>1 ≤ n ≤ 10<sup>5<br></sup>0 ≤ left.length, right.length ≤ n + 1<br>0 ≤ left[i], right[i] ≤ n<br>1 ≤ left.length + right.length ≤ n + 1<br>All values of left and right are unique, and each value can appear only in one of the two arrays.

## Expected Complexities
- Time Complexity: O(n + m)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Greedy` `Arrays`
- **Company Tags:** `Google`

### Related Articles
- [Last Moment Before All Ants Fall Out Of A Plank](https://www.geeksforgeeks.org/last-moment-before-all-ants-fall-out-of-a-plank/)
