<h1 align="center">Maximum Sub-String after at most K changes</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.88%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 16K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

We have a string <b>s</b> of length <b>n</b>, which contains only <b>UPPERCASE</b> characters and we have a number <b>k</b> (always less than <b>n</b>). We can make at most <b>k</b> changes in our string. In one change, you can replace any <b>s[i] </b>(0<= i < n) with any uppercase character (from 'A' to 'Z'). After <b>k</b> changes, find the maximum possible length of the sub-string which have all same characters.

<b>Example 1:</b>

<pre><b>Input: </b>s = "ABAB", k = 2
<b>Output: </b>4
<b>Explanation: </b>Change 2 'B' into 'A'. 
Now s = "AAAA"

</pre>

<b>Example:</b>

<pre><b>Input: </b>s = "ADBD", k = 1
<b>Output: </b>3
<b>Explanation: </b>Change 'B' into 'D'.
Now s = "ADDD"

</pre>

<b>Your Task:</b><br>You don't need to read or print anything. Your task is to complete the function <b>characterReplacement() </b>which takes <b>s</b> and <b>k</b> as input parameters and returns the maximum length of sub-string after doing k changes.<br> 

<b>Expected Time Complexity: </b>O(n)<br><b>Expected Space Complexity: </b>O(26)<br> 

<b>Constraints:</b><br>1 <= n <= 10<sup>5</sup><br>0 <= k < n


<hr>

### Tags
- **Topic Tags:** `Misc`
- **Company Tags:** `Amazon`

### Related Articles
- [Maximum Length Substring Having All Same Characters After K Changes](https://www.geeksforgeeks.org/maximum-length-substring-having-all-same-characters-after-k-changes/)
