<h1 align="center">Job Sequencing Problem</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 59.45%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 22K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a set of <b>N</b> jobs where each <b>job<sub>i</sub></b> has a deadline and profit associated with it. Each job takes <b><i>1</i></b> unit of time to complete and only one job can be scheduled at a time. We earn the profit if and only if the job is completed by its deadline. The task is to find the number of jobs done and the <b>maximum profit</b>.

<b>Note: </b>Jobs will be given in the form (Job<sub>id</sub>, Deadline, Profit) associated with that Job.<br><b>Example 1:</b>

<pre><b>Input:
</b>N = 4
Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
<b>Output:
</b>2 60<b>
Explanation:
</b>Since at deadline 1 Job3 can give the maximum profit and for deadline 4 we left with only Job1 hence<b> </b>Job<sub>1</sub> and Job<sub>3 </sub>can be done with maximum profit of 60 (20+40).
</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>N = 5
Jobs = {(1,2,100),(2,1,19),(3,2,27),
        (4,1,25),(5,1,15)}
<b>Output:
</b>2 127<b>
Explanation:
</b>2 jobs can be done with
maximum profit of 127 (100+27).</pre>

<b>Your Task</b> :<br>You don't need to read input or print anything. Your task is to complete the function <b>JobScheduling()</b> which takes an integer <b>N</b> and an array of Jobs(Job id, Deadline, Profit) as input and returns an array <b>ans[ ] </b>in which<b> ans[0] contains</b> <b>the count of jobs and</b> <b>ans[1] contains maximum profit</b>.

<b>Expected Time Complexity</b>: O(NlogN)<br><b>Expected Auxilliary Space</b>: O(N)

<b>Constraints:</b><br>1 <= N <= 10<sup>5</sup><br>1 <= Deadline <= N<br>1 <= Profit <= 500


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Greedy` `Algorithms`
- **Company Tags:** `Accolite` `Microsoft`

### Related Interview Experiences
- [Accolite Interview Experience Set 15 Campus](https://www.geeksforgeeks.org/accolite-interview-experience-set-15-campus/)
- [Microsoft Interview Experience For Software Engineering Internship 2019](https://www.geeksforgeeks.org/microsoft-interview-experience-for-software-engineering-internship-2019/)
