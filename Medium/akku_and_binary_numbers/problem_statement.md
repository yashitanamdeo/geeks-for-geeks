<h1 align="center">Akku and Binary Numbers</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.0%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 19K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Akku likes binary numbers and she likes playing with these numbers. Her teacher once gave her a question.For given value of  L and R, Akku have to find the count of number X, which have only three-set bits in it's binary representation such that "L ≤ X ≤ R".Akku is genius, she solved the problem easily. Can you do it ??

<b>Example 1:</b>

<pre><b>Input</b>:
L = 11 and R = 19 
<b>Output:</b> 4
<b>Explanation</b>:
There are 4 such numbers with 3 set bits in 
range 11 to 19.
11 -> 1011
13 -> 1101
14 -> 1110
19 -> 10011</pre>

 

<b>Example 2:</b>

<pre><b>Input:</b>
L = 25 and R = 29
<b>Output: 3
</b><b>Explanation</b>:
There are 3 such numbers with 3 set bits in
range 25 to 29. 
25 -> 11001 
26 -> 11010 
28 -> 11100
</pre>

<br>
<b>Your Task:  </b><br>
You don't need to read input or print anything. Your task is to complete the function <b>solve()</b> which takes the integer <b>L</b> and <b>R</b> as input parameters and returns the count of number X, which have only three-set bits in its binary representation such that "L ≤ X ≤ R".<br>
<br>
<b>Expected Time Complexity:</b> O(63<sup>3</sup>) + O(log(R-L))<br>
<b>Expected Auxiliary Space:</b> O(63<sup>3</sup>)

<br>
<b>Constraints:</b><br>
1 ≤ L ≤ R ≤ 10<sup>18</sup>


<hr>

### Tags
- **Topic Tags:** `Bit Magic` `Binary Search` `Data Structures` `Algorithms`
- **Company Tags:** `None`
