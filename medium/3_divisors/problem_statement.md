<h1 align="center">3 Divisors</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 11.17%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 45K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a list of <b>q</b> queries, and for each query, an integer <b>n</b> is provided. The task is to find how many numbers less than or equal to <b>n</b> have exactly <b>3 divisors</b>.

<b>Examples:</b>

<pre><b>Input: </b>q = 1<br>          query[0] = 6
<b>Output: </b>1
<b>Explanation: </b>There is only one number 4 which has exactly three divisors 1, 2 and 4 and less than equal to 6.</pre>

<pre><b>Input: </b>q = 2
       query[0] = 6
       query[1] = 10
<b>Output: </b>1
        2
<b>Explanation: </b>For query 1 it is covered in the example 1. query 2:There are two numbers 4 and 9 having exactly 3 divisors and less than <br>equal to 10.</pre>

<b>Constraints : </b><br>1 <= q <= 10<sup>3</sup><br>1 <= query[i] <= 10<sup>12</sup>

## Expected Complexities
- Time Complexity: O(q*n*log(log(n)))
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Mathematical` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Find All Factors Of A Natural Number In Sorted Order](https://www.geeksforgeeks.org/find-all-factors-of-a-natural-number-in-sorted-order/)
- [Numbers Exactly 3 Divisors](https://www.geeksforgeeks.org/numbers-exactly-3-divisors/)
