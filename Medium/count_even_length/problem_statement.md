<h1 align="center">Count even length</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 41.34%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 24K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a number n, find count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.<br>The anwer can be very large. So, you have to return answer modulo 10<sup>9</sup>+7.

<b>Example:</b>

<pre><b>Input: </b>n = 2
<b>Output: </b>6
<b>Explanation: </b>There are 6 sequences of length 
2*n, the sequences are 0101, 0110, 1010, 1001, 
0000 and 1111.</pre>

<b>Example:</b>

<pre><b>Input: </b>n = 1
<b>Output: </b>2
<b>Explanation: </b>There are 2 sequence of length 
2*n, the sequence are 00 and 11.
</pre>

 

<b>Your Task:</b><br>You don't need to read or print anyhting. Your task is to complete the function <b>compute_value()</b> which takes n as input parameter and returns count of all binary sequence of length 2*n such that sum of first n bits is same as sum of last n bits modulo 10<sup>9</sup> + 7.<br> 

<b>Expected Time Complexity: </b>O(n * log(n))<br><b>Expected Space Complexity:  </b>O(1)<br> 

<b>Constraints:</b><br>1 <= n <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Count Even Length Binary Sequences With Same Sum Of First And Second Half Bits](https://www.geeksforgeeks.org/count-even-length-binary-sequences-with-same-sum-of-first-and-second-half-bits/)
