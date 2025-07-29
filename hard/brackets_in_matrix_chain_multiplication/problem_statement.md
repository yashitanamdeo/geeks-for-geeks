<h1 align="center">Brackets in Matrix Chain Multiplication</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 59.66%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 34K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 25m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[]</b> of length <b>n </b>used to denote the dimensions of a series of <b>matrices</b> such that the dimension of <b>i'th</b> matrix is <b>arr[i] * arr[i+1]</b>. There are a total of <b>n-1</b> matrices. Find the most efficient way to multiply these matrices together. <br>As in [<i><b>MCM</b></i>](https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/), you were returning the most effective count but this time return the <b>string</b> which is formed of <b>A - Z </b>(only Uppercase) denoting matrices & <b>Brackets</b>( <b>"("</b> <b>")"</b> ) denoting multiplication symbols. For example, if n =11, the matrixes can be denoted as A - K as n<=26 & brackets as multiplication symbols.

<b>NOTE:</b>

1. Each multiplication is denoted by putting <b>open & closed</b> brackets to the matrices multiplied & also, please note that the order of matrix multiplication matters, as matrix multiplication is non-commutative <b>A*B != B*A</b>
1. As there can be <b>multiple</b> possible answers, the console would print "<b>true</b>" for the <b>correct</b> string and "<b>false</b>" for the <b>incorrect</b> string. You need to only return a <b>string</b> that performs a minimum number of multiplications.
<b>Examples:</b>

<pre><b>Input:</b> arr[] = [40, 20, 30, 10, 30]
<b>Output:</b> true
<b>Explanation:</b> Let's divide this into matrix(only 4 are possible) [ [40, 20] -> A, [20, 30] -> B, [30, 10] ->C, [10, 30] -> D ]<br>First we perform multiplication of B & C -> (BC), then we multiply A to (BC) -> (A(BC)), then we multiply D to (A(BC)) -> ((A(BC))D)<br>so the solution returned the string <b>((A(BC))D)</b>, which performs minimum multiplications. The total number of multiplications are 20*30*10 + 40*20*10 + 40*10*30 = 26,000.<br></pre>

<pre><b>Input:</b> arr[] = [10, 20, 30]
<b>Output:</b> true
<b>Explanation:</b> There is only one way to multiply two matrices: (AB): The cost for the multiplication will be 6000
</pre>

<pre><b>Input:</b> arr = [3, 3, 3]
<b>Output:</b> true
<b>Explanation:</b> The solution returned the string <b>(AB)</b>, which performs minimum multiplications. The total number of multiplications are (3*3*3) = 27.</pre>

<b>Constraints:</b><br>2 ≤ arr.size() ≤ 26 <br>1 ≤ arr[i] ≤ 100

## Expected Complexities
- Time Complexity: O(n^3)
- Auxiliary Space: O(n^2)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Matrix` `Data Structures` `Algorithms`
- **Company Tags:** `Microsoft`

### Related Articles
- [Printing Brackets Matrix Chain Multiplication Problem](https://www.geeksforgeeks.org/printing-brackets-matrix-chain-multiplication-problem/)

### Related Interview Experiences
- [Microsoft Interview Experience Set 128 Campus Internship](https://www.geeksforgeeks.org/microsoft-interview-experience-set-128-campus-internship/)
