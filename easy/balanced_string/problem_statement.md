<h1 align="center">Balanced string</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.5%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 18K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an integer N.Create a string using only lowercase characters from a to z that follows the given rules.

<b>When N is even:</b>

Use N/2 characters from the beginning of a-z and N/2 characters from the ending of a-z.

When N is greater than 26,continue repeating the instructions until length of string becomes N.

<b>When N is odd:</b>

<i>Case 1:</i> If the sum of digits of N is even, Select (N+1)/2 characters from the beginning of a-z and (N-1)/2 characters from the ending of a-z.

<i>Case 2:</i> If the sum of digits of N is odd, Select (N-1)/2 characters from the beginning of a-z and (N+1)/2 characters from the ending of a-z.

When N is greater than 26,continue repeating the instructions until length of string becomes N.

 

<b>Example 1:</b>

<pre><b>Input:</b> 
N=21
<b>Output:</b> 
abcdefghijpqrstuvwxyz
<b>Explanation:
</b>Since 21 is odd and sum of digits
of 21 is also odd,we take (21-1)/2=10 
characters from the beginning and 
(21+1)/2=11 characters from the 
end of a-z.</pre>

<b>Example 2:</b><b> </b>

<pre><b>Input:
</b>N=28 <b>
Output:</b> 
abcdefghijklmnopqrstuvwxyzaz
<b>Explanation:</b> 
Since 28>26, we keep repeating 
the process until length of string becomes 
28.</pre>

 

<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>BalancedString() </b>which takes the integer N as input parameter and returns the string created using given procedures.<br>
 

<b>Expected Time Complexity: </b>O(N)<br>
<b>Expected Auxiliary Space: </b>O(1)<br>
 

<b>Constraints:</b><br>
1 <= N <= 10<sup>5</sup><br>


<hr>

### Tags
- **Topic Tags:** `Strings` `implementation` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Program For Sum Of The Digits Of A Given Number](https://www.geeksforgeeks.org/program-for-sum-of-the-digits-of-a-given-number/)
