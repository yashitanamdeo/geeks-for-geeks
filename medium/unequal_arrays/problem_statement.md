<h1 align="center">Unequal Arrays</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 55.61%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 23K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given two arrays <b>A </b>and <b>B </b>each of length <b>N</b>. You can perform the following operation on array<i> A</i> zero or more times. 

- Select any two indices <b>i</b> and <b>j</b>, <b>1 <= i , j <= N </b>and <b>i != j</b>
- Set <b>A[i] </b>= <b>A[i] </b>+ <b>2 </b>and <b>A[j] = A[j]-2 </b>
Find the <b>minimum </b>number of operations required to make A and B <b>equal</b>.

<i>Note :</i>

- Two arrays are said to be equal if the frequency of each element is equal in both of them.
- Arrays may contain duplicate elements.
<b>Example 1:</b>

<pre><b>Input</b>:
N = 3
A[] = {2, 5, 6}
B[] = {1, 2, 10}
<b>Output:</b> 2
<b>Explanation</b>: 
Select i = 3, j = 2, A[3] = 6 + 2 = 8 and A[2] = 5 - 2 = 3
Select i = 3, j = 2, A[3] = 8 + 2 = 10 and A[2] = 3 - 2 = 1
Now A = {2, 1, 10} and B = {1, 2, 10}</pre>

<b>Example 2:</b>

<pre><b>Input</b>:
N = 2
A[] = {3, 3}
B[] = {9, 8}
<b>Output:</b> -1
<b>Explanation</b>: 
It can be shown that <b>A </b>cannot be made equal to <b>B</b>.</pre>

<b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>solve()</b> which takes the 2 arrays <b>A[]</b>, <b>B[]</b> and their size <b>N </b>as input parameters and returns the <b>minimum </b>number of moves to make A and B equal if possible else return <b>-1</b>.

<b>Expected Time Complexity:</b> O(NlogN)<br><b>Expected Auxiliary Space:</b> O(N)

<b>Constraints:</b><br>1 <= N <= 10<sup>5</sup><br>-10<sup>9</sup> <= A[i] <= 10<sup>9</sup><br>-10<sup>9</sup> <= B[i] <= 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Algorithms` `logical-thinking`
- **Company Tags:** `None`
