<h1 align="center">Minimum times A has to be repeated such that B is a substring of it</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 47.6%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 17K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two strings <b>A </b>and<b> B. </b>Find minimum number of times A has to be repeated such that B is a Substring of it. If <b>B</b> can never be a substring then return <b>-1</b>.

 

<b>Example 1:</b>

<pre><b>Input:
</b>A = "abcd"
B = "cdabcdab"
<b>Output:
</b>3
<b>Explanation:</b>
Repeating A three times (“abcdabcdabcd”),
B is a substring of it. B is not a substring
of A when it is repeated less than 3 times.
</pre>

<b>Example 2:</b>
<pre><b>Input:
</b>A = "ab"
B = "cab"
<b>Output :</b>
-1
<b>Explanation:</b>
No matter how many times we repeat A, we can't
get a string such that B is a substring of it.
</pre>

<br>
<b>Your Task:  </b><br>
You don't need to read input or print anything. Your task is to complete the function <b>minRepeats()</b> which takes 2 strings A, and B respectively and returns the minimum number of times A has to be repeated such that B is a substring of it. Return -1 if it's not possible.

<br>
<b>Expected Time Complexity:</b> O(|A| * |B|)<br>
<b>Expected Auxiliary Space:</b> O(|B|)

<br>
<b>Constraints:</b><br>
1 ≤ |A|, |B| ≤ 10<sup>3</sup>
String A and B consists of lower case alphabets


<hr>

### Tags
- **Topic Tags:** `Searching` `Strings` `Pattern Searching` `Data Structures` `Algorithms`
- **Company Tags:** `Google`

### Related Articles
- [Minimum Number Of Times A Has To Be Repeated Such That B Is A Substring Of It](https://www.geeksforgeeks.org/minimum-number-of-times-a-has-to-be-repeated-such-that-b-is-a-substring-of-it/)

### Related Interview Experiences
- [Google Interview Experience Set 7 Software Engineering Intern](https://www.geeksforgeeks.org/google-interview-experience-set-7-software-engineering-intern/?ref=rp)
