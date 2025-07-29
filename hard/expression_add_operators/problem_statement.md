<h1 align="center">Expression Add Operators</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 61.49%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 22K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 40m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>s</b> that contains only digits (0-9) and an integer <b>target</b>, return <b>all possible</b> strings by inserting the binary operator <b>' + '</b>, <b>' - '</b>, or <b>' * '</b> between the digits of <b>s</b> such that the resultant expression evaluates to the <b>target</b> value. If no such expression is possible, return an <b>empty list</b>.

<b>Note</b>:

1. <b> </b>Operands in the returned expressions <b>should not</b> contain leading zeros. For example, 2 + 03 is not allowed whereas 20 + 3 is fine. 
1. It is <b>allowed</b> to not insert any of the operators.
1. Driver code will print the final list of strings in <b>lexicographically smallest order</b>.
<b>Examples:</b>

<pre><b>Input: </b>s = "124", target = 9<br><b>Output: </b>["1+2*4"]<br><b>Explanation:</b> The valid expression that evaluate to 9 is 1 + 2 * 4</pre>

<pre><b>Input: </b>s = "125", target = 7<br><b>Output: </b>["1*2+5", "12-5"]<br><b>Explanation:</b> The two valid expressions that evaluate to 7 are 1 * 2 + 5 and 12 - 5.</pre>

<pre><b>Input: </b>s = "12", target = 12<br><b>Output:</b> ["12"] <br><b>Explanation:</b> s itself matches the target. No other expressions are possible.</pre>

<pre><b>Input: </b>s = "987612", target = 200<br><b>Output:</b> []<br><b>Explanation:</b> There are no expressions that can be created from "987612" to evaluate to 200.</pre>

<b>Constraints:</b><br>1 ≤ s.size() ≤ 10<br>s consists of only digits.<br>-2<sup>31 </sup>≤ target ≤ 2<sup>31</sup>-1

## Expected Complexities
- Time Complexity: O(4 ^ n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Strings` `Recursion` `Backtracking` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Print All Possible Expressions That Evaluate To A Target](https://www.geeksforgeeks.org/print-all-possible-expressions-that-evaluate-to-a-target/)
