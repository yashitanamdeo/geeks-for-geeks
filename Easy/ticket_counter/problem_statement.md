<h1 align="center">Ticket Counter</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 55.31%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 33K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

<b>n</b> people from 1 to n are standing in the queue at a movie ticket counter. It is a weird counter, as it distributes tickets to the <b>first k</b> people and then the <b>last k </b>people and again first k people and so on, once a person gets a ticket moves <b>out</b> of the queue. The task is to find the <b>last</b> person to get the ticket.

<b>Examples:</b>

<pre><b>Input: </b>n = 9, k = 3<br><b>Output: </b>6<br><b>Explanation:</b><br>Starting queue will like [1, 2, 3, 4, 5, 6, 7, 8, 9]. After the first distribution queue will look like [4, 5, 6, 7, 8, 9].<br>And after the second distribution queue will look like [4, 5, 6]. The last person to get the ticket will be 6.</pre>

<pre><b>Input:</b> n = 5, k = 1<br><b>Output: </b>3<br><b>Explanation:</b><br>Queue start as [1, 2, 3, 4, 5] -> [2, 3, 4, 5] -> [2, 3, 4] -> [3, 4] -> [3]<br>Last person to get ticket will be 3.</pre>

<b>Constraints:</b><br>1 ≤  k ≤  n  ≤ 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Greedy` `Queue`
- **Company Tags:** `None`

### Related Articles
- [Find Out The Person Who Got The Ticket Last](https://www.geeksforgeeks.org/find-out-the-person-who-got-the-ticket-last/)
