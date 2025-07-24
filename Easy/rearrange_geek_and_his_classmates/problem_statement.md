<h1 align="center">Rearrange Geek and his Classmates</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 58.05%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 14K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Geek and his classmates are playing a prank on their Computer Science teacher. They change places every time the teacher turns to look at the blackboard. 

Each of the <b>N</b> students in the class can be identified by a unique roll number <b>X </b>and each desk has a number <b>i </b>associated with it. Only one student can sit on one desk. <br>
Each time the teacher turns her back, a student with roll number X sitting on desk number i gets up and takes the place of the student with roll number i.

If the current position of <b>N</b> students in the class is given to you in an array, such that<b> i</b> is the desk number and <b>a[i]</b> is the roll number of the student sitting on the desk, can you modify <b>a[ ] </b>to represent the next position of all the students?<br>
<b>Note: </b>The array a[ ] will be a permutation of the array : {0, 1, 2, 3, ...., n-1}.

<br>
<b>Example 1:</b>

<pre><b>Input:</b>
N = 6
a[] = {0, 5, 1, 2, 4, 3}
<b>Output: </b>0 3 5 1 4 2
<b>Explanation: </b>After reshuffling, the modified 
position of all the students would be 
{0, 3, 5, 1, 4, 2}.</pre>

<br>
<b>Example 2:</b>

<pre><b>Input:</b>
N = 5
a[] = {4, 3, 2, 1, 0}
<b>Output:</b> 0 1 2 3 4 
<b>Explanation:</b> After reshuffling, the modified 
position of all the students would be 
{0, 1, 2, 3, 4}.</pre>

<br>
<b>Your Task:  </b><br>
You dont need to read input or print anything. Complete the function <b>prank() </b>which takes the array <b>a[ ]</b> and its size <b>N</b> as input parameters and modifies the array in-place to reflect the new arrangement.

<br>
<b>Expected Time Complexity:</b> O(N)<br>
<b>Expected Auxiliary Space:</b> O(1)<br>
 

<b>Constraints:</b><br>
1 ≤ N ≤ 10<sup>5</sup><br>
0 ≤ a[i] ≤ N-1


<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures`
- **Company Tags:** `None`
