<h1 align="center">Special Palindrome Substrings</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 60.12%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 18K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two strings s1 and s2, The task is to convert s1 into a palindrome such that s1 contain s2 as a substring in a minimum number of operation.<br>
In a single operation, we can replace any word of s1 with any character.

<b>Note: </b>If it is not possible to convert s1 such that it is a palindrome as well as contains substring of s2, then return -1.

<b>Example 1:</b>

<pre><b>Input:</b>
s1="abaa" s2="bb"
<b>Output:</b> 1
<b>Explanation:</b>
we can replace s1[2]='a' with 'b'.
So the new s1 will be like "abba",
having s2 as a substring.
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
s1="abbd" s2="mr"
<b>Output:</b> 4
<b>Explanation:</b>
1st: s1="mrbd" --> 2 operations (this is the 
minimum operation to make s2 a substring of s1) 
2nd: s1="mrrm" --> 2 operations 
(this is the minimum operation to make s1 palindrome)
</pre>

<b>Your Task:  </b><br>
You don't need to read input or print anything. Complete the function <b>specialPalindrome()</b> which takes the two strings <b>s1</b> and <b>s2</b> as input parameters. Return the minimum number of operations needs to convert s1 such that it is a palindrome and having s2 as a substring in s1.

<b>Expected Time Complexity: </b>O(N*M) [N: size of s1 and M: size of s2]<br>
<b>Expected Auxiliary Space:</b> O(N)

<b>Constraints:</b><br>
1 ≤ |s2| ≤ |s1| ≤  1000


<hr>

### Tags
- **Topic Tags:** `Strings` `Data Structures`
- **Company Tags:** `MakeMyTrip`

### Related Interview Experiences
- [Makemytrip Interview Experience Fte](https://www.geeksforgeeks.org/makemytrip-interview-experience-fte/)
