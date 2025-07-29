<h1 align="center">Is it Fibonacci</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.86%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 27K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Geek just learned about Fibonacci numbers. 


The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...<br>
where the next number is found by adding up the two numbers before it.


He defines a new series called Geeky numbers. Here the next number is the sum of the <b>K</b> preceding numbers.<br>
You are given an array of size K, <b>GeekNum[ ], </b>where the i<sup>th</sup> element of the array represents the i<sup>th</sup> Geeky number. Return its N<sup>th</sup> term.

<b>Note: </b>This problem can be solved in O(N<sup>2</sup>) time complexity but the user has to solve this in O(N). The Constraints are less because there can be integer overflow in the terms.

<b>Example 1:</b>

<pre><b>Input</b>:
N = 6, K = 1
GeekNum[] = {4}
<b>Output:</b> 
4
<b>Explanation</b>: 
Terms are 4, 4, 4, 4, 4, 4</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N = 5, K = 3
GeekNum[] = {0, 1, 2}
<b>Output: 
</b>6
<b>Explanation</b>: 
Terms are 0, 1, 2, 3, 6.
So the 5th term is 6
</pre>

<b>Your Task:  </b><br>
You don't need to read input or print anything. Your task is to complete the function <b>solve( )</b> which takes integer N, K, and an array GeekNum[] as input parameters and returns the Nth term of the Geeky series.

<b>Expected Time Complexity: O(N)<br>
Expected Space Complexity: O(N)</b>

<b>Constraints:</b><br>
1 ≤ K <u><</u> 30<br>
1 ≤ N ≤ 70<br>
K ≤ N<br>
0 <u><</u> GeekNum[ ] <u><</u> 100


<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures` `sliding-window`
- **Company Tags:** `None`
