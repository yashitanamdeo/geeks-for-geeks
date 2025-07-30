<h1 align="center">Minimum Cost To Make Two Strings Identical</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 52.29%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 34K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two strings <b>x</b> and <b>y</b>, and two values <b>costX</b> and <b>costY</b>, the task is to find the minimum cost required to make the given two strings identical. You can delete characters from both the strings. The cost of deleting a character from string X is costX and from Y is costY. The cost of removing all characters from a string is the same.

<b>Example 1:</b>

<pre><b>Input: </b>x = "abcd", y = "acdb", costX = 10 
       costY = 20.
<b>Output:</b> 30
<b>Explanation: </b>For Making both strings 
identical we have to delete character 
'b' from both the string, hence cost 
will be = 10 + 20 = 30.</pre>

<b>Example 2:</b>

<pre><b>Input : </b>x = "ef", y = "gh", costX = 10
        costY = 20.
<b>Output: </b>60
<b>Explanation: </b>For making both strings 
identical, we have to delete 2-2 
characters from both the strings, hence 
cost will be = 10 + 10 + 20 + 20 = 60.
</pre>

<b>Your Task:</b><br>You don't need to read or print anything. Your task is to complete the function <b>findMinCost() </b>which takes both strings and the costs as input parameters and returns the minimum cost.

<b>Expected Time Complexity: </b>O(|x|*|y|)<br><b>Expected Space Complexity: </b>O(|x|*|y|)

<b>Constraints:</b><br>1 ≤ |x|, |y| ≤ 1000<br>1<= costX, costY <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Minimum Cost Make Two Strings Identical](https://www.geeksforgeeks.org/minimum-cost-make-two-strings-identical/)
