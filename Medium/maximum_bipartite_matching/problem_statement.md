<h1 align="center">Maximum Bipartite Matching</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 58.2%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 17K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There are M job applicants and N jobs.  Each applicant has a subset of jobs that he/she is interested in. Each job opening can only accept one applicant and a job applicant can be appointed for only one job. Given a matrix <b>G</b> with <b>M</b> rows and <b>N</b> columns where G(i,j) denotes i<sup>th </sup>applicant is interested in the j<sup>th </sup>job. Find the maximum number of applicants who can get the job.

<b>Example 1:</b>

<pre><b>Input: 
</b>M = 3, N = 5
G = {{1,1,0,1,1},{0,1,0,0,1},
{1,1,0,1,1}}
<b>Output: </b>3
<b>Explanation: </b>There is one of the possible
assignment-
First applicant gets the 1st job.
Second applicant gets the 2nd job.
Third applicant gets the 4th job.
</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>M = 6, N = 2
G = {{1,1},{0,1},{0,1},{0,1},
{0,1},{1,0}}
<b>Output: </b>2
<b>Explanation: </b>There is one of the possible
assignment-
First applicant gets the 1st job.
Second applicant gets the 2nd job.
</pre>

 

<b>Your Task:</b><br>You don't need to read to print anything. Your task is to complete the function <b>maximumMatch() </b>which takes matrix G as input parameter and returns the maximum number of applicants who can get the job.

<b>Expected Time Complexity:</b> O(N<sup>3</sup>).<br><b>Expected Auxiliary Space:</b> O(N).

<b>Constraints:</b><br>1 ≤ N, M ≤ 100


<hr>

### Tags
- **Topic Tags:** `Graph` `Data Structures`
- **Company Tags:** `None`
