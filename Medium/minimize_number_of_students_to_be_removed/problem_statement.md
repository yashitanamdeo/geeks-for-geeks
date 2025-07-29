<h1 align="center">Minimize number of Students to be removed</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.16%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 24K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

<b>N</b> Students of different heights are attending an assembly. The heights of the students are represented by an array<b> </b><b>H[]. </b>The problem is that if a student has less or equal height than the student standing in front of him, then he/she cannot see the assembly. Find the minimum number of students to be removed such that all the remaining students can see the assembly.<br>
 

<b>Example 1:</b>

<pre><b>Input:
</b>N = 6
H[] = {9, 1, 2, 3, 1, 5}
<b>Output:
</b>2
<b>Explanation:</b>
We can remove the students at 0 and 4th index.
which will leave the students with heights
1,2,3, and 5.
</pre>

<b>Example 2:</b>
<pre><b>Input:
</b>N = 3
H[] = {1, 2, 3} 
<b>Output :</b>
0
<b>Explanation:</b>
All of the students are able to see the
assembly without removing anyone.
</pre>

<br>
<b>Your Task:  </b><br>
You don't need to read input or print anything. Your task is to complete the function <b>removeStudents()</b> which takes an integer N and an array H[ ] of size N as input parameters and returns the minimum number of students required to be removed to enable all the remaining students to see the assembly.

<br>
<b>Expected Time Complexity:</b> O(N logN)<br>
<b>Expected Auxiliary Space:</b> O(N)

<br>
<b>Constraints:</b><br>
1 ≤ N ≤ 10<sup>5</sup><br>
1 ≤ H[i] ≤ 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `Microsoft`

### Related Articles
- [Longest Monotonically Increasing Subsequence Size N Log N](https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/)

### Related Interview Experiences
- [Microsoft Full Time Interview Experience On Campus](https://www.geeksforgeeks.org/microsoft-full-time-interview-experience-on-campus/?ref=rp)
