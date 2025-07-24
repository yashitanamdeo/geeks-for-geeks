<h1 align="center">Form a number divisible by 3 using array digits</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 63.96%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 80K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 10m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You will be given an array <b>arr</b> of integers of length <b>N. </b>You can construct an integer from two integers by treating the integers as strings, and then concatenating them. For example, <b>19 </b>and <b>4</b> can be used to construct <b>194 </b>and <b>419. </b>

The task is to find whether it’s possible to construct an integer using all the digits of these numbers such that it would be <b>divisible by 3</b>. <br>If it is possible then print <b>1</b> and if not print <b>0</b>.

<b>Example 1:</b>

<pre><b>Input:</b> N = 3
arr = {40, 50, 90}
<b>Output:</b> 1
<b>Explanation:</b> One such number is 405090.</pre>

<b>Example 2:</b>

<pre><b>Input:</b> N = 2
arr = {1, 4}
<b>Output:</b> 0
<b>Explanation:</b> The numbers we can form 
are 14 and 41. But neither of them are 
divisible by 3.</pre>

<b>Your Task:</b><br>You do not need to read input or print anything. Your task is to complete the function <b>isPossible()</b> which takes <b>N</b> and <b>arr</b> as input parameters and returns <b>1 i</b>f we can form a number by the digits of the given number, that would be divisible by 3, otherwise returns <b>0</b>.

<b>Expected Time Complexity:</b> O(N)<br><b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>1 ≤ N, arr[i] ≤ 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Mathematical` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Possible To Make A Divisible By 3 Number Using All Digits In An Array](https://www.geeksforgeeks.org/possible-to-make-a-divisible-by-3-number-using-all-digits-in-an-array/)
