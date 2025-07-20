<h1 align="center">Substrings of length k with k-1 distinct elements</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 57.85%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 41K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>s</b> consisting only lowercase alphabets and an integer <b>k</b>. Find the <b>count</b> of all substrings of length <b>k</b> which have exactly <b>k-1 </b>distinct characters.

<b>Examples:</b>

<pre><b>Input: </b>s = "abcc", k = 2<br><b>Output: </b>1<br><b>Explaination: </b>Possible substring of length k = 2 are,<br>ab : 2 distinct characters<br>bc : 2 distinct characters<br>cc : 1 distinct characters<br>Only one valid substring so, count is equal to 1.</pre>

<pre><b>Input: </b>"aabab", k = 3<br><b>Output:</b> 3<br><b>Explaination:</b> Possible substring of length k = 3 are, <br>aab : 2 distinct charcters<br>aba : 2 distinct characters<br>bab : 2 distinct characters<br>All these substring are valid so, the total count is equal to 3.</pre>

<b>Constrains:</b><br>1 ≤ s.size() ≤ 10<sup>5<br></sup>2 ≤ k ≤ 27

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `sliding-window` `Strings` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon`

### Related Articles
- [Count Of Substrings Of Length K With Exactly K Distinct Characters](https://www.geeksforgeeks.org/count-of-substrings-of-length-k-with-exactly-k-distinct-characters/)

### Related Interview Experiences
- [Amazon Interview Experience For Sde 1 Full Time Referral 2020](https://www.geeksforgeeks.org/amazon-interview-experience-for-sde-1-full-time-referral-2020/)
