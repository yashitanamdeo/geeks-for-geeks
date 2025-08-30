<h1 align="center">The Celebrity Problem</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 38.33%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 342K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

A celebrity is a person who is known to all but <b>does not know</b> anyone at a party. A party is being organized by some people. A square matrix <b>mat[][] </b>of size n*n is used to represent people at the party such that if an element of row<b> i </b>and column<b> j </b>is<b> set to 1</b> it means <b>ith person knows jth person</b>. You need to return the <b>index </b>of the<b> celebrity</b> in the party, if the celebrity does not exist, return <b>-1</b>.

<b>Note:</b> Follow <b>0-based </b>indexing.

<b>Examples:</b>

<pre><b>Input: </b>mat[][] = [[1, 1, 0],<br>                [0, 1, 0],<br>                [0, 1, 1]]
<b>Output:</b> 1
<b>Explanation: </b>0th and 2nd person both know 1st person and 1st person does not know anyone. Therefore, 1 is the celebrity person.</pre>

<pre><b>Input: </b>mat[][] = [[1, 1], <br>                [1, 1]]
<b>Output:</b> -1
<b>Explanation: </b>Since both the people at the party know each other. Hence none of them is a celebrity person.</pre>

<pre><b>Input: </b>mat[][] = [[1]]
<b>Output:</b> 0</pre>

<b>Constraints:</b><br>1 ≤ mat.size() ≤ 1000<br>0 ≤ mat[i][j] ≤ 1<br>mat[i][i] = 1

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Stack` `Data Structures` `two-pointer-algorithm`
- **Company Tags:** `Zoho` `Flipkart` `Amazon` `Microsoft` `Google` `Fab.com` `One97` `United Health Group`

### Related Articles
- [The Celebrity Problem](https://www.geeksforgeeks.org/the-celebrity-problem/)
