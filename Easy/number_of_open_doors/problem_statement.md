<h1 align="center">Number Of Open Doors</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 36.15%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 60K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Consider a long alley with a <b>n </b>number of doors on one side. All the doors are closed initially. You move to and fro in the alley changing the states of the doors as follows: you open a door that is already closed and you close a door that is already opened. You start at one end go on altering the state of the doors till you reach the other end and then you come back and start altering the states of the doors again.<br>In the first go, you alter the states of doors numbered 1, 2, 3, , n.<br>In the second go, you alter the states of doors numbered 2, 4, 6<br>In the third go, you alter the states of doors numbered 3, 6, 9 <br>You continue this till the Nth go in which you alter the state of the door numbered N.<br>You have to find the number of open doors at the end of the procedure.

<b>Example :</b>

<pre><b>Input: n =</b> 2
<b>Output: </b>1
<b>Explanation: </b>Following the sequence 4 times, we can see that only 1st door will remain open.</pre>

<pre><b>Input: n =</b> 4
<b>Output: </b>2
<b>Explanation: </b>Following the sequence 4 times, we can see that only 1st and 4th doors will remain open.</pre>

<b>Constraints:</b><br>1 <= n <= 10<sup>9</sup>

## Expected Complexities
- Time Complexity: O(log(n))
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Mathematical` `Algorithms`
- **Company Tags:** `TCS`

### Related Articles
- [Check Door Open Closed](https://www.geeksforgeeks.org/check-door-open-closed/)
