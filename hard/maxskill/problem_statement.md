<h1 align="center">MaxSkill</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 60.89%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 16K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 45m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a queue of<b> n </b>people indexed from <b>0</b> to <b>n-1</b>. Each person has a <b>rating </b>represented by an array <b>arr[]</b><b>.</b> You are asked to remove all the persons from the queue. If you remove the<b> i-th </b>person from the queue, you gain a skill value of <b>arr[i - 1] * arr[i] * arr[i + 1]</b>. Return the <b>maximum total</b> skill you can obtain by removing the people optimally.

Note: If <b>i - 1</b> or <b>i + 1</b> is out of bounds, assume there is an implicit person with a rating of <b>1 </b>at that position.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [5, 10] 
<b>Output:</b> 60
<b>Explanation:</b><br>Remove person with rating 5 → Skill gained = 1 * 5 * 10 = 50, remaining queue: [10].
Remove person with rating 10 → Skill gained = 1 * 10 * 1 = 10, total skill = 50 + 10 = 60.</pre>

<pre><b>Input: </b>arr[] = [3, 2, 5, 8]<b>
Output: </b>182<b>
Explanation:
</b>Remove person with rating 2 → Skill gained = 3 * 2 * 5 = 30, remaining queue: [3, 5, 8].
Remove person with rating 5 → Skill gained = 3 * 5 * 8 = 120, remaining queue: [3, 8].
Remove person with rating 3 → Skill gained = 1 * 3 * 8 = 24, remaining queue: [8].
Remove person with rating 8 → Skill gained = 1 * 8 * 1 = 8, total skill = 30 + 120 + 24 + 8 = 182</pre>

<b>Constraints:</b><br>1 ≤ n ≤ 300<br>0 ≤ arr[i] ≤ 100

## Expected Complexities
- Time Complexity: O(n^3)
- Auxiliary Space: O(n^2)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Dynamic Programming` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Burst Balloon To Maximize Coins](https://www.geeksforgeeks.org/burst-balloon-to-maximize-coins/)
