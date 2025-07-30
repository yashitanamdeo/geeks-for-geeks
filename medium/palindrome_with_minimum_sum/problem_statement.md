<h1 align="center">Palindrome with minimum sum</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 60.42%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 21K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string, <b>S</b>.The string can contain small case<b> </b>English letters or <b>'?'</b>. You can replace '?' with any small English letter. Now if it is possible to make the string <b>S</b> a palindrome after replacing all '?' then find the palindromic string with a <b>minimum ascii sum</b> of the absolute difference of adjacent characters. Otherwise, return -1.

<b>Example 1:</b>

<pre><b>Input: S = </b>a???c??c????
<b>Output: </b>4<b>
Explanation:
</b>We can see that we can make the string
palindrome. Now to get <b>minimum</b> <b>ascii</b> <b>sum</b> we should
replace all the '?' between 'a' and 'c' with
'b' and all the '?' between two 'c' with 'c'.
So after replacing all the '?' the string: 
<b>abbbccccbbba</b>.
The sum of differences of adjacent characters is 4.<b>   </b></pre>

<b>Example 2:</b>

<pre><b>Input: S = </b>a???c??c???c<b>
Output: </b>-1
<b>Explanation:
</b>It is not possible to make the string palindrome.</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>minimumSum() </b>which takes a string S input parameter and returns an integer denoting the sum of differences of adjacent characters. If it is not possible to make string palindrome, return -1. 

<b>Expected Time Complexity:</b> O(N)<br><b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>1 <= |S| <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Strings` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Minimize Adjacent Character Differences In Palindromic String With](https://www.geeksforgeeks.org/minimize-adjacent-character-differences-in-palindromic-string-with/)
