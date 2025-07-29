<h1 align="center">Complement</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.0%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 19K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a binary string <b>str</b>. In a single operation, you can choose two indices <b>L</b> and <b>R</b> such that <b>1 ≤ L ≤ R ≤ N</b> and complement the characters between <b>L</b> and <b>R</b> i.e <b>str<sub>L</sub>, str<sub>L+1</sub>, , str<sub>R</sub></b>. By complement, we mean change character <b>0</b> to <b>1</b> and vice-versa. 

You task is to perform <b>ATMOST</b> one operation such that in final string number of <b>1</b>s is maximised. If there is no need to completement, i.e., string contains all <b>1</b>s, return <b>-1</b>. Else, return the two values denoting <b>L</b> and <b>R</b>. If there are multiple solutions, return the <b>lexicographically smallest pair of L and R</b>.

<b>Example 1:</b>

<pre><b>Input:
</b>N = 3
str = "111"
<b>Output:</b> -1
<b>Explanation:</b> As all characters are '1', 
so don't need to complement any.
</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>N = 2
str = "01"
<b>Output:</b> 1 1
<b>Explanation:</b> After complementing [1, 1] 
the string becomes "11".
</pre>

<b>Your Task:</b><br>You don't need to read input or print anything<b>. </b>Complete the function <b>findRange()</b> which takes the string <b>str</b> and the size of the string, <b>n</b>, as input parameters and returns an array of length 2 or 1 representing the answer. <br>You don't have to print answer or take inputs.

<b>Expected Time Complexity:</b> O(N)<br><b>Expected Auxiliary Space:</b> O(1)<br><br><b>Constraints:</b><br>1 ≤ N ≤ 10<sup>5</sup><br>Str is a binary string i.e. contains only '0' and '1'.


<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures`
- **Company Tags:** `Amazon`

### Related Articles
- [Largest Sum Contiguous Subarray](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/)
