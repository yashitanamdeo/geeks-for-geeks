<h1 align="center">Fill up buckets</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.2%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 18K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given <b>n</b> buckets and infinite number of balls. The maximum capacity of each bucket is given in an array <b>capacity[]</b>. Find the number of ways to fill the buckets with balls such that each bucket has <b>atleast 1</b> ball and all the buckets have <b>distinct</b> number of balls in them.<br><b>Note: </b>Since the answer may be very large, calculate the answer modulo <b>10^9+7.</b>

<b>Example 1:</b>

<pre><b>Input: 
</b>n = 1
capacity = [6]
<b>Output: </b>6
<b>Explanation: </b>Since there is only one 
bucket. It may hold any number of balls 
ranging from 1 to 6.

</pre>

<b>Example 2:</b>

<pre><b>Input: 
</b>n = 2 
capacity = [5, 8]
<b>Output: </b>35
<b>Explanation: </b>If the first bucket has 1
ball in it then the second bucket cant have 1 
ball, so the second bucket has 8-1 = 7 choices.
So the first bucket has 5 choices and for each
choice second bucket has 7 choices.
So total there are 35 ways.
</pre>

 

<b>Your Task:</b><br>You don't need to read or print anything. Your task is to complete the function <b>totalWays()</b> which takes <b>n</b> and <b>capacity[]</b> as input parameters and returns the <b>number of possible ways</b> to fill the buckets. Since the answer may be very large, calculate the answer modulo <b>10^9+7.</b>

<b>Expected Time Complexity: </b>O(n*log(n)) <br><b>Expected Space Complexity: </b>O(1)

<b>Constraints:</b><br>1 <= n <= 100000<br>1 <= capacity[i] <= 100000


<hr>

### Tags
- **Topic Tags:** `permutation` `Combinatorial`
- **Company Tags:** `None`

### Related Articles
- [Maximum Number Of Buckets That Can Be Filled](https://www.geeksforgeeks.org/maximum-number-of-buckets-that-can-be-filled/)
