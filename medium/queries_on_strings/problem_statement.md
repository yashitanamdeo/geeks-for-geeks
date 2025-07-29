<h1 align="center">Queries on Strings</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 55.84%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 8K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>str</b> you have to answer several queries on that string. In each query you will be provided two values <b>L</b> and <b>R</b> and you have to find the number of <b>distinct</b> characters in the sub string from index <b>L</b> to index <b>R</b> (inclusive) of the original string.<br> 

<b>Example 1:</b>

<pre><b>Input: </b>str = "abcbaed",
Query = {{1,4},{2,4},{1,7}}
<b>Output: </b>{3,2,5}
<b>Explanation: </b>For the first query distinct 
characters from [1, 4] are a, b and c.
For the second query distinct characters from
[2, 4] are b and c.
For the third query distinct characters from
[1, 7] are a, b, c, d and e.
</pre>

 

<b>Your Task:</b><br>You don't need to read or print anyhting. Your task is to complete the function <b>SolveQueries() </b>which takes str and Query as input parameter and returns a list containing answer for each query.<br> 

<b>Expected Time Complexity: </b>O(max(26*length of str, 26 * No of queries))<br><b>Expected Space Complexity: </b>O(26 * length of str)<br> 

<b>Constraints:</b><br>1 <= |str| <= 10<sup>5</sup><br>1 <= No of Queries <= 10<sup>4</sup><br>1 <= L<sub>i</sub> <= R<sub>i</sub> <= |str|


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Print All Distinct Characters Of A String In Order 3 Methods](https://www.geeksforgeeks.org/print-all-distinct-characters-of-a-string-in-order-3-methods/)
