<h1 align="center">All Unique Permutations of an array</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 52.85%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 43K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[] </b>of length <b>n. </b>Find all possible <b>distinct permutations </b>of the array in <b>sorted order</b>. A sequence <b>A </b>is greater than sequence <b>B</b> if there is an index <b>i </b>for which <b>A<sub>j</sub> = B<sub>j</sub></b> for all <b>j<i </b>and <b>A<sub>i</sub> > B<sub>i</sub></b>.

<b>Examples:</b>

<pre><b>Input</b>: arr[] = [1, 3, 3]
<b>Output</b>: [[1, 3, 3], [3, 1, 3], [3, 3, 1]]
<b>Explanation</b>: These are the only possible distinct permutations for the given array.
</pre>

<pre><b>Input</b>: arr[] = [4, 5]
<b>Output</b>: [[4, 5], [5, 4]]<br><b>Explanation:</b> These are the only possible distinct permutations for the given array.
</pre>

<b>Constraints:</b><br>1 ≤ n ≤ 9

## Expected Complexities
- Time Complexity: O(n! * n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Recursion` `Backtracking` `Algorithms`
- **Company Tags:** `Google`

### Related Articles
- [Print All Possible Permutations Of An Array With Duplicates Using Backtracking](https://www.geeksforgeeks.org/print-all-possible-permutations-of-an-array-with-duplicates-using-backtracking/)
