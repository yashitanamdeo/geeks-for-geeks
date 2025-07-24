<h1 align="center">Count Unique Vowel Strings</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.99%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 17K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a lowercase string <b>s</b>, determine the total number of distinct strings that can be formed using the following rules:

- Identify all<b> unique </b>vowels (a, e, i, o, u) present in the string.
- For each distinct vowel, choose <b>exactly one </b>of its occurrences from s. If a vowel appears multiple times, each occurrence represents a unique selection choice.
- Generate all possible permutations<b> </b>of the selected vowels. Each unique arrangement counts as a distinct string.
Return the total number of such distinct<b> </b>strings.

<b>Examples:</b>

<pre><b>Input: </b>s<b> </b>=<b> </b>"aeiou"<b><br>Output: </b>120<b><br>Explanation: </b>Each vowel appears once, so the number of different strings can form is 5! = 120.</pre>

<pre><b>Input: </b>s<b> </b>= "ae"<b><br>Output: </b>2<b><br>Explanation: </b>Pick a and e, make all orders → "ae", "ea".</pre>

<pre><b>Input:</b> s = "aacidf"<br><b>Output: </b>4 <br><b>Explanation:</b> Vowels in s are 'a' and 'i', Pick each 'a' once with a single 'i', make all orders → "ai", "ia", "ai", "ia".</pre>

<b>Constraints:<br></b>1 ≤ s.size() ≤ 100

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Strings` `Combinatorial` `Mathematical`
- **Company Tags:** `None`

### Related Articles
- [Unique Vowel Arrangements](https://www.geeksforgeeks.org/unique-vowel-arrangements/)
