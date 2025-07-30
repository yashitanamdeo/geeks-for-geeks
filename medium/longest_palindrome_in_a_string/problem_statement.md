<h1 align="center">Longest Palindrome in a String</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 23.2%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 336K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>s</b>, your task is to find the longest palindromic substring within s. 


A <b>substring</b> is a <b>contiguous </b>sequence of characters within a string, defined as s[i...j] where 0 ≤ i ≤ j < len(s).

A <b>palindrome</b> is a string that reads the <b>same </b>forward and backward. More formally, s is a palindrome if reverse(s) == s.


<b>Note:</b> If there are multiple palindromic substrings with the same length, return the <b>first occurrence</b> of the longest palindromic substring from left to right.

<b>Examples :</b>

<pre><b>Input: </b>s = “forgeeksskeegfor” <b>
Output: </b>“geeksskeeg”<b>
Explanation: </b>There are several possible palindromic substrings like “kssk”, “ss”, “eeksskee” etc. But the substring “geeksskeeg” is the longest among all.</pre>

<pre><b>Input: </b>s = “Geeks” <b>
Output: </b>“ee”
<b>Explanation</b>: "ee" is the longest palindromic substring of "Geeks". </pre>

<pre><b>Input: </b>s = “abc” <b>
Output: </b>“a”
<b>Explanation</b>: "a", "b" and "c" are longest palindromic substrings of same length. So, the first occurrence is returned.</pre>

<b>Constraints:</b><br>1 ≤ s.size() ≤ 10<sup>3<br>s consist of only lowercase English letters.<br></sup>

## Expected Complexities
- Time Complexity: O(n^2)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Strings` `Dynamic Programming` `palindrome` `Data Structures` `Algorithms`
- **Company Tags:** `Zoho` `Accolite` `Amazon` `Microsoft` `Samsung` `MakeMyTrip` `Visa` `Walmart` `Google` `Qualcomm` `Groupon`

### Related Articles
- [Longest Palindromic Substring Using Dynamic Programming 2](https://www.geeksforgeeks.org/longest-palindromic-substring-using-dynamic-programming-2/)
- [Longest Palindromic Substring](https://www.geeksforgeeks.org/longest-palindromic-substring/)

### Related Interview Experiences
- [Accolite Interview Experience Set 4 On Campus](https://www.geeksforgeeks.org/accolite-interview-experience-set-4-on-campus/)
- [Amazon Interview Experience Set 412 Sde Ii](httpss://www.geeksforgeeks.org/amazon-interview-experience-set-412-sde-ii/)
- [Samsung Research Institute Bangalore Srib Intern](https://www.geeksforgeeks.org/samsung-research-institute-bangalore-srib-intern/)
