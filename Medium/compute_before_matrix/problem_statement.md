<h1 align="center">Compute Before Matrix</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 78.27%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 5K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

For a given 2D Matrix <b>before,</b> the corresponding cell (x, y) of the <b>after</b> matrix is calculated as follows: 


<pre>res = 0;
for(i = 0; i <= x; i++){
    for( j = 0; j <= y; j++){              
        res += before(i,j);
    }
}
after(x,y) = res;
</pre>


 

Given an <b>N*M </b>2D-Matrix <b>after,</b> your task is to find the corresponding <b>before </b>matrix for the given matrix.

 

<b>Example 1:</b>

<pre><b>Input:</b>
N = 2, M = 3
after[][] = {{1, 3, 6},
            {3, 7, 11}}
<b>Output:</b>
1 2 3
2 2 1
<b>Explanation:</b>
The before matrix for the given after matrix
matrix is {{1, 2, 3}, {2, 2, 1}}.
Reason:
According to the code given in problem,
after(0,0) = before(0,0) = 1
after(0,1) = before(0,0) + before(0,1)
= 1 + 2 = 3.
after(0, 2) = before(0,0) + before(0, 1)
+ before(0, 2) = 1 + 2 + 3 = 6.
Similarly we can calculate values for every
cell of the after matrix.
</pre>

 

<b>Example 2:</b>

<pre><b>Input: </b>
N = 1, M = 3
after[][] = {{1, 3, 5}}
<b>Output:</b>
1 2 2
<b>Explanation: </b>
The before matrix for the given after matrix
is {{1, 2, 2}}.</pre>

<b>Your Task:</b><br>
Complete the function <b>c</b><b>omputeBeforeMatrix() </b>which takes the integers <b>N</b>, <b>M, </b>and the 2D Matrix <b>after</b> as the input parameters, and returns the before matrix of the given after matrix.

<b>Expected Time Complexity:</b> O(N*M)<br>
<b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>
1 ≤ N, M, after[i][j]  ≤  10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `prefix-sum` `Matrix` `Data Structures` `Algorithms`
- **Company Tags:** `Dunzo`

### Related Articles
- [Compute Before Matrix](https://www.geeksforgeeks.org/compute-before-matrix/)

### Related Interview Experiences
- [Dunzo Interview Experience For Software Engineer 2](https://www.geeksforgeeks.org/dunzo-interview-experience-for-software-engineer-2/)
