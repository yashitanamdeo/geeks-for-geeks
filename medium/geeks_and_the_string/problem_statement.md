<h1 align="center">Geeks And The String</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.91%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 24K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Our geek loves to play with strings, Currently, he is trying to reduce the size of a string by recursively removing all the consecutive duplicate pairs. In other words, He can apply the below operations any number of times.

- Remove all the consecutive duplicate pairs and concatenate the remaining string to replace the original string.
Your task is to find the string with minimum length after applying the above operations.

<b>Note: </b>If the string length become zero after applying operations, return "-1" as a string.

<br>
<b>Example 1:</b>

<pre><b>Input</b>:
aaabbaaccd
<b>Output</b>: 
ad
<b>Explanation</b>: 
Remove (aa)abbaaccd =>abbaaccd
Remove a(bb)aaccd => aaaccd
Remove (aa)accd => accd
Remove a(cc)d => ad
</pre>

<b>Example 2:</b>

<pre><b>Input</b>: 
aaaa
<b>Output</b>: 
Empty String
<b>Explanation</b>: 
Remove (aa)aa => aa
Again removing pair of duplicates then (aa) 
will be removed and we will get 'Empty String'.
</pre>

<br>
<b>Your Task:</b><br>
This is a <b>function </b>problem. You only need to <b>complete </b>the function<b> removePair() </b>that takes a <b>string </b>as a <b>parameter</b> and <b>returns </b>the <b>modified string</b>. Return "-1" if the whole string is deleted.

<b>Expected Time Complexity:</b> O(N)<br>
<b>Expected Auxiliary Space:</b> O(N)<br>
<br>
<b>Constraints:</b><br>
1 <= |str| <= 10<sup>4</sup>


<hr>

### Tags
- **Topic Tags:** `Stack` `Data Structures`
- **Company Tags:** `None`
