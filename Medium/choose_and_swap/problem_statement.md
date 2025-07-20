<h1 align="center">Choose and Swap</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 22.67%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 78K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a string <b>str</b> of lower case english alphabets. You can choose any two characters in the string and replace all the occurences of the first character with the second character and replace all the occurences of the second character with the first character. Your aim is to find the lexicographically smallest string that can be obtained by doing this operation at most once.

<b>Examples:</b>

<pre><b>Input</b>: str = "ccad"
<b>Output:</b> "aacd"
<b>Explanation</b>: In ccad, we choose a and c and after doing the replacement operation once we get, aacd and this is the lexicographically smallest string possible. </pre>

<pre><b>Input: </b>str = "abba"
<b>Output: </b>"abba"
<b>Explanation: </b>In abba, we can get baab after doing the replacement operation once for a and b but that is not lexicographically smaller than abba. So, the answer is abba. </pre>

<b>Expected Time Complexity: </b>O(|str|) <b><br>Expected Auxiliary Space: </b>O(1)<b><br><br>Constraints:</b><br>1<= |str| <=10<sup>5</sup>

<b>Note : </b>Here |str| refers to the length of the string str.


<hr>

### Tags
- **Topic Tags:** `Greedy` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Swap All Occurrences Of Two Characters To Get Lexicographically Smallest String](https://www.geeksforgeeks.org/swap-all-occurrences-of-two-characters-to-get-lexicographically-smallest-string/)
