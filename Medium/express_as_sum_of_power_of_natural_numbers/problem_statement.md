<h1 align="center">Express as sum of power of natural numbers</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 45.35%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 33K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two numbers<b> n</b> and <b>x</b>, find out the total number of ways <b>n</b> can be expressed as the sum of<b> the Xth</b> power of <b>unique natural numbers</b>. As the total number of ways can be very large, so return the number of ways modulo 10<sup>9 </sup>+ 7. 

<b>Example 1:</b>

<pre><b>Input</b>: <br>n = 10, x = 2
<b>Output:</b> <br>1 
<b>Explanation</b>: <br>10 = 1<sup>2</sup> + 3<sup>2</sup>, Hence total 1 possibility. 
</pre>

<b>Example 2:</b>

<pre><b>Input: <br></b>n = 100, x = 2
<b>Output: <br></b>3
<b>Explanation</b>: <br>100 = 10<sup>2</sup> 
6<sup>2</sup> + 8<sup>2</sup> and 1<sup>2</sup> + 3<sup>2</sup> + 4<sup>2</sup> + 5<sup>2</sup> + 7<sup>2</sup> 
Hence total 3 possibilities. 
</pre>

<b>Your Task:  </b><br>You don't need to read input or print anything. Complete the function <b>numOfWays() </b>which takes n and x as input parameters and returns the total number of ways n can be expressed as the sum of xth power of unique natural numbers.<br>

<b>Expected Time Complexity:</b> O(n<sup>2</sup>logn)<br><b>Expected Auxiliary Space:</b> O(n)<br>

<b>Constraints:</b><br>1 <= n <= 10<sup>3</sup><br>1 <= x <= 5


<hr>

### Tags
- **Topic Tags:** `Mathematical` `Recursion` `Algorithms` `Dynamic Programming`
- **Company Tags:** `Adobe`

### Related Articles
- [Find Ways Integer Can Expressed Sum N Th Power Unique Natural Numbers](https://www.geeksforgeeks.org/find-ways-integer-can-expressed-sum-n-th-power-unique-natural-numbers/)
