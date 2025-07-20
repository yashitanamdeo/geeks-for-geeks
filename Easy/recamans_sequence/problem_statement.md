<h1 align="center">Recamans sequence</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.31%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 44K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an integer <b>n</b>, return the first n elements of [<i><b>Recaman’s sequence</b></i>](http://mathworld.wolfram.com/RecamansSequence.html).<br>It is a function with domain and co-domain as whole numbers. It is recursively defined as below:<br>Specifically, let a(n) denote the (n+1)<sup>th</sup> term. (0 being the 1<sup>st</sup> term).<br>The rule says:<br>a(0) = 0<br>a(n) = a(n-1) - n, if a(n-1) - n > 0 and is not included in the sequence previously<br>       =  a(n-1) + n otherwise. 

<b>Example 1:</b>

<pre><b>Input:</b> <br>n = 5
<b>Output:</b> <br>0 1 3 6 2
<b>Explaination:</b> <br>a(0) = 0,<br>a(1) = a(0)-1 = 0-1 = -1 and -1<0, therefore a(1) = a(0)+1 = 1,<br>a(2) = a(1)-2 = 1-2 = -1 and -1<0, therefore a(2) = a(1)+2 = 3,<br>a(3) = a(2)-3 = 3-3 = 0 but since 0 is already present in the sequence, a(3) = a(2)+3 = 3+3 = 6,<br>a(4) = a(3)-4 = 6-4 = 2.<br>Therefore the first 5 elements of Recaman's sequence will be 0 1 3 6 2.</pre>

<b>Example 2:</b>

<pre><b>Input:</b> <br>n = 3
<b>Output:</b> <br>0 1 3
<b>Explaination:</b> <br>As seen in example 1, the first three elements will be 0 1 3.</pre>

<b>Your Task:</b><br>You do not need to read input or print anything. Your task is to complete the function <b>recamanSequence()</b> which takes <b>n</b> as the input parameter and returns the sequence.

<b>Expected Time Complexity:</b> O(n)<br><b>Expected Auxiliary Space:</b> O(n)

<b>Constraints:</b><br>1 ≤ n ≤ 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Hash` `Mathematical` `Recursion` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Recamans Sequence](https://www.geeksforgeeks.org/recamans-sequence/)
