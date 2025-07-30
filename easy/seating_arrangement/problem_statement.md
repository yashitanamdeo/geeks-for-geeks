<h1 align="center">Seating Arrangement</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 49.85%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 49K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an integer <b>n</b>, denoting the number of people who needs to be seated, and a list of <b>m</b> integers <b>seats</b>, where <b>0</b> represents a vacant seat and <b>1</b> represents an already occupied seat.

Find whether all <b>n</b> people can find a seat, provided that no two people can sit next to each other.

<b>Example 1:</b>

<pre><b>Input:</b>
n = 2
m = 7
seats[] = {0, 0, 1, 0, 0, 0, 1}
<b>Output:</b>
Yes
<b>Explanation:</b>
The two people can sit at index 0 and 4.
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
n = 1
m = 3
seats[] = {0, 1, 0}
<b>Output:</b>
No
<b>Explanation:</b>
There is no way to get a seat for one person.
</pre>

<b>Your Task:</b>

You don't have to input or print anything. Complete the function <b>is_possible_to_get_seats() </b>which takes the input parameters and return a boolean value, indicating whether all people can find a seat.

<b>Expected Time Complexity: O(m)<br>
Expected Space Complexity: O(1)</b>

<b>Constraints:</b>

- 0 <= n <= 10<sup>5</sup>
- 1 <= m <= 10<sup>5</sup>
- seats[i] == 0 or seats[i] == 1


<hr>

### Tags
- **Topic Tags:** `Arrays` `Greedy`
- **Company Tags:** `None`
