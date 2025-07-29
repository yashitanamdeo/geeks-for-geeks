<h1 align="center">Divide in Incremental Groups</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 64.3%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 19K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two integers <b>N</b> and <b>K</b>, the task is to count the number of ways to divide <b>N</b> into groups of <b>positive integers</b>. Such that <b>each group</b> shall have <b>K elements</b> and their <b>sum is N</b>. Also the number of elements in the groups follows a <b>non-decreasing</b> order <b>(i.e. group[i] <= group[i+1])</b>. Find the number of such groups

<b>Example 1:</b>

<pre><b>Input:</b>
N = 8
K = 4
<b>Output:</b>
5
<b>Explanation:</b>
There are 5 groups such that their sum is 8 
and the number of positive integers in each 
group is 4. The 5 groups are [1, 1, 1, 5], 
[1, 1, 2, 4], [1, 1, 3, 3], [1, 2, 2, 3] and 
[2, 2, 2, 2].</pre>

<b>Example 2:</b>

<pre><b>Input: </b>
N = 4
K = 3
<b>Output:</b>
1
<b>Explanation: </b>
The only possible grouping is {1, 1, 2}. Hence,
the answer is 1 in this case.</pre>

<b>Your Task:</b><br>
Complete the function <b>countWaystoDivide</b><b>() </b>which takes the integers <b>N</b> and <b>K </b>as the input parameters, and returns the number of ways to divide the sum <b>N </b>into<b> K </b>groups.

<b>Expected Time Complexity:</b> O(N<sup>2</sup>*K)<br>
<b>Expected Auxiliary Space:</b> O(N<sup>2</sup>*K)

<b>Constraints:</b><br>
1 ≤ K ≤ N ≤ 100


<hr>

### Tags
- **Topic Tags:** `Mathematical` `Algorithms`
- **Company Tags:** `Expedia`

### Related Articles
- [Count The Number Of Ways To Divide N In K Groups Incrementally](https://www.geeksforgeeks.org/count-the-number-of-ways-to-divide-n-in-k-groups-incrementally/)

### Related Interview Experiences
- [Expedia Coding Round Experience Intern 2021](https://www.geeksforgeeks.org/expedia-coding-round-experience-intern-2021/)
- [Expedia Interview Experience](https://www.geeksforgeeks.org/expedia-interview-experience/)
- [Expedia Group Interview Experience For Sde Internship Off Campus](https://www.geeksforgeeks.org/expedia-group-interview-experience-for-sde-internship-off-campus/)
