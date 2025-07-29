<h1 align="center">Prefix match with other strings</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.02%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 39K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of strings <b>arr[]</b> of size <b>n, </b>a string <b>str</b> and an integer <b>k</b>. The task is to find the count of strings in <b>arr[]</b> whose <b>prefix of length</b> <b>k</b> matches with the <b>k-length prefix</b> of <b>str</b>.

<b>Examples<br></b>

<pre><b>Input</b>: n = 6 arr[] = {“abba”, “abbb”, “abbc”, “abbd”, “abaa”, “abca”} str = “abbg” k = 3
<b>Output:</b> 4 
<b>Explanation</b>: “abba”, “abbb”, “abbc” and “abbd” have their prefix of length 3 equal to 3-length prefix of <b>str</b> i.e., <b>"abb".</b></pre>

<pre><b>Input: </b>n = 3 arr[] = {“geeks”, “geeksforgeeks”, “forgeeks”} str = “ge” k = 5
<b>Output: </b>0<br><b>Explanation</b>: There do not exists any prefix of <b>str</b> with length <b>5.</b> So, there are no matches possible.</pre>

<b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>klengthpref()</b> which takes the array of strings arr[], its size <b>n </b>and an integer <b>k, </b>a string<b> str </b>as input parameters and returns the count of strings in <b>arr[]</b> whose prefix of length <b>k</b> matches with the <b>k</b> length prefix of <b>str</b>.

<b>Expected Time Complexity:</b> O(n*l) where l is the length of the longest word in arr[].<br><b>Expected Auxiliary Space:</b> O(n*l) where l is the length of the longest word in arr[].<br>

<b>Constraints:</b><br>1 <= n <= 1000<br>1<sup> </sup><= |arr[i]| , |str| <= 1000<br>1 <= k <= 1000<br>arr[i], str must contain only lowercase English alphabets<br>


<hr>

### Tags
- **Topic Tags:** `Strings` `Trie` `Data Structures` `Advanced Data Structure`
- **Company Tags:** `Samsung`

### Related Articles
- [Count Of Strings Whose Prefix Match With The Given String To A Given Length K](https://www.geeksforgeeks.org/count-of-strings-whose-prefix-match-with-the-given-string-to-a-given-length-k/)

### Related Interview Experiences
- [Samsung Research Institute Bangalore Interview Experience On Campus For Internship](https://www.geeksforgeeks.org/samsung-research-institute-bangalore-interview-experience-on-campus-for-internship/)
