<h1 align="center">Task Scheduler</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 58.08%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 29K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a character array <b>tasks</b> of size <b>N</b>, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.<br>CPU has a cooldown period for each task. CPU can repeat a task only after atleast <b>K </b>units of time has passed after it did same task last time. It can perform other tasks in that time, can stay idle to wait for repeating that task.

Return the <b>least</b> number of units of times that the CPU will take to finish all the given tasks.

<b>Example 1:</b>

<pre><b>Input:</b><br>N = 6<br>K = 2<br>task[ ] = {'A', 'A', 'A', 'B', 'B', 'B'}<br><b>Output: </b>8<br><b>Explanation:</b> <br>A -> B -> idle -> A -> B -> idle -> A -> B<br>There is atleast 2 units of time between any two same tasks.<br> </pre>

<b>Example 2:</b>

<pre><b>Input:</b><br>N = 12<br>K = 2<br>task[ ] = {'A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'}<br><b>Output: </b>16<br><b>Explanation:</b>  <br>One possible solution is <br>A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A.</pre>

 

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>leastInterval()</b> which takes the interger <b>N</b>, integer <b>K</b> and an character array <b>tasks </b>as parameters and returns the minimum unit of time required to complete all tasks.

<b>Expected Time Complexity:</b> O(N)<br><b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>1 ≤ N ≤ 10<sup>4</sup><br>0 ≤ K ≤ 100<br>task<sub>i </sub>is upper-case English letter.


<hr>

### Tags
- **Topic Tags:** `Arrays` `Hash` `Greedy` `Data Structures` `Algorithms`
- **Company Tags:** `None`
