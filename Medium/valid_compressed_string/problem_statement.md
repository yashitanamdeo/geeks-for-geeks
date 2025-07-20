<h1 align="center">Valid Compressed String</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.0%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 33K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

A special compression mechanism can arbitrarily delete 0 or more characters and replace them with the deleted character count.<br>
Given two strings, <b>S</b> and <b>T</b> where S is a normal string and T is a compressed string, determine if the compressed string  T is valid for the plaintext string S. <br>
<b>Note: </b>If T consists of multiple integers adjacently, consider all of them at a single number. For example T="12B32", consider T as "12" + "B" + "32".  

<br>
<b>Example 1:</b>

<pre><b>Input:
</b>S = "GEEKSFORGEEKS"
T = "G7G3S"
<b>Output:
</b>1
<b>Explanation:</b>
We can clearly see that T is a valid 
compressed string for S.
</pre>

<br>
<b>Example 2:</b>

<pre><b>Input:
</b>S = "DFS"
T = "D1D"
<b>Output :</b>
0
<b>Explanation:</b>
T is not a valid compressed string.
</pre>

<br>
<b>Your Task:  </b><br>
You don't need to read input or print anything. Your task is to complete the function <b>checkCompressed()</b> which takes 2 strings S and T as input parameters and returns integer 1 if T is a valid compression of S and 0 otherwise.

<br>
<b>Expected Time Complexity:</b> O(|T|)<br>
<b>Expected Auxiliary Space:</b> O(1)

<br>
<b>Constraints:</b><br>
1 ≤ |S| ≤ 10<sup>6</sup><br>
1 ≤ |T| ≤ 10<sup>6</sup><br>
All characters are either capital or numeric.


<hr>

### Tags
- **Topic Tags:** `Strings` `Greedy` `Data Structures` `Algorithms`
- **Company Tags:** `Facebook`

### Related Articles
- [Valid Compressed String](https://www.geeksforgeeks.org/valid-compressed-string/)

### Related Interview Experiences
- [Facebook Nyc Onsite Interview Experience](https://www.geeksforgeeks.org/facebook-nyc-onsite-interview-experience/)
