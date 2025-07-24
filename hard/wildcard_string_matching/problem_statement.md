<h1 align="center">Wildcard string matching</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 23.88%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 64K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 25m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two strings <b>wild</b> and <b>pattern</b>. Determine if the given two strings can be matched given that, <b>wil</b><b>d</b> string may contain <b>*</b> and <b>?</b> but string <b>pattern </b>will not. *<b> </b>and <b>?</b> can be converted to another character according to the following rules:

<pre>* --> This character in string wild can be replaced by any sequence of characters, it can also be replaced by an empty string.
? --> This character in string wild can be replaced by any one character.</pre>

<b>Example 1:</b>

<pre><b>Input: <br></b>wild = ge*ks<br>pattern = geeks
<b>Output: </b>Yes
<b>Explanation:</b> Replace the '*' in wild string 
with 'e' to obtain pattern "geeks".</pre>

<b>Example 2:</b>

<pre><b>Input: <br></b>wild =<b> </b>ge?ks*<br>pattern = geeksforgeeks
<b>Output:</b> Yes
<b>Explanation:</b> Replace '?' and '*' in wild string with
'e' and 'forgeeks' respectively to obtain pattern 
"geeksforgeeks"
</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>match() </b>which takes<b> </b>the string <b>wild</b> and <b>pattern</b> as input parameters and returns <b>true</b> if the string <b>wild </b>can be made equal to the string <b>pattern</b>, otherwise, returns <b>false</b>.

<b>Expected Time Complexity:</b> O(length of wild string * length of pattern string)<br><b>Expected Auxiliary Space:</b> O(length of wild string * length of pattern string)

<b>Constraints:</b><br>1 <= length of the two string <= 10^3


<hr>

### Tags
- **Topic Tags:** `Strings` `Data Structures`
- **Company Tags:** `Amazon` `Ola Cabs`

### Related Articles
- [Wildcard Character Matching](https://www.geeksforgeeks.org/wildcard-character-matching/)

### Related Interview Experiences
- [Ola Interview Experience Set 6 For Sde 1](https://www.geeksforgeeks.org/ola-interview-experience-set-6-for-sde-1/)
