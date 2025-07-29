<h1 align="center">Minimum Days</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 54.28%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 22K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string S of length N containing only lowercase alphabets. You are also given a permutation P of length N containing integers from 0 to N-1. In (i+1)'th day you can take the P[i] value of the permutation array and replace S[P[i]] with a '?'.

For example in day 1, we can choose index of permutation array is i=0 and replace S[P[0]] with '?'.<br>
Similarly in day 2, we can choose index of permutation array is i=1. You can replace S[P[1]] with '?'.<br>
Similarly in day 3,we can choose index of permutation array is i=2. You can replace S[P[2]] with '?'.

You have to tell the minimum number of days required, such that after it for all index i (0<=i<N-1), if S[i]!='?', then S[i]!=S[i+1].

<b>Example 1:</b>

<pre><b>Input:</b>
N = 4
S = "aabb"
P[] = {2, 1, 3, 0}
<b>Output:</b> 2
<b>Explanation:</b> In day 1, we replace S[P[0]] with '?'. 
After that String S = "aa?b". As we can see S 
still has character 'a' at index 0 and 1.
In day 2, we replace S[P[1]] with '?'. After 
that String S = "a??b". As we can see the String 
has for all index i (0<=i<N-1), if S[i]!='?', then S[i]!=S[i+1].</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N = 4
S = "abca"
P[] = {3, 0, 2, 1}
<b>Output:</b> 0
<b>Explanation:</b> We can see that the initial string 
S = "abca" has for all index i (0<=i<N-1), if S[i]!='?', then S[i]!=S[i+1].</pre>

<b>Your Task: </b><br>
You don't need to read input or print anything. Your task is to complete the function getMinimumDays() which takes the string S, array P[] and its size N as input parameters and returns the minimum number of days required such that string satisfies with the condition given earlier.

<b>Expected Time Complexity:</b> O(n).<br>
<b>Expected Auxiliary Space:</b> O(1).

<b>Constraints:</b>

1 <= N <= 10<sup>5</sup><br>
0 <= P[i] <= N-1<br>
S contains only lowercase alphabets.


<hr>

### Tags
- **Topic Tags:** `Strings` `permutation` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Minimum Days To Achieve The String](https://www.geeksforgeeks.org/minimum-days-to-achieve-the-string/)
