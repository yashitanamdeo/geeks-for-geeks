<h1 align="center">Balancing Consonants and Vowels Ratio</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 58.77%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 9K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array of strings <b>arr[], </b>where each <b>arr[i] </b>consists of lowercase english alphabets. You need to find the number of <b>balanced strings</b> in <b>arr[]</b> which can be formed by <b>concatinating</b> one or more contiguous strings of arr[].<br>A balanced string contains the equal number of <b>vowels</b> and <b>consonants</b>. 

<b>Examples:</b>

<pre><b>Input: </b>arr[] = ["aeio", "aa", "bc", "ot", "cdbd"]<br><b>Output: </b>4<b><br>Explanation: </b>arr[0..4], arr[1..2], arr[1..3], arr[3..3] are the balanced substrings with equal consonants and vowels.</pre>

<pre><b>Input: </b>arr[] = ["ab", "be"]<br><b>Output: </b>3<b><br>Explanation: </b>arr[0..0], arr[0..1], arr[1..1] are the balanced substrings with equal consonants and vowels.</pre>

<pre><b>Input: </b>arr[] = ["tz", "gfg", "ae"]<br><b>Output: </b>0<b><br>Explanation: </b>There is no such balanced substring present in arr[] with equal consonants and vowels.<br></pre>

<b>Constraints:<br></b>1 ≤ arr.size() ≤ 10<sup>5</sup><br>1 ≤ arr[i].size() ≤ 10<sup>5</sup><br>Total number of lowercase english characters in arr[] is lesser than 10<sup>5</sup>.

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `prefix-sum` `Strings` `Hash`
- **Company Tags:** `None`

### Related Articles
- [Balance Consonant And Vowels Ratio](https://www.geeksforgeeks.org/balance-consonant-and-vowels-ratio/)
