<h1 align="center">Pairs of Non Coinciding Points</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 46.31%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 8K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

In a given cartesian plane, there are <b>N</b> points. We need to find the Number of Pairs of  points(<b>A, B</b>) such that

- Point A and Point B do not coincide.
- Manhattan Distance and the Euclidean Distance between the points should be equal.
<b>Note:</b> Pair of 2 points(A,B) is considered different from  Pair of 2 points(B ,A).<br>
Manhattan Distance = |x2-x1|+|y2-y1|<br>
Euclidean Distance   = ((x2-x1)^2 + (y2-y1)^2)^0.5, where points are (x1,y1) and (x2,y2).

 

<b>Example 1:</b>

<pre><b>Input:</b>
<b>N = </b>2
<b>X = </b>{1, 7}
<b>Y = </b>{1, 5}
<b>Output:</b>
0
<b>Explanation:</b>
None of the pairs of points have
equal Manhatten and Euclidean distance.</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
<b>N = </b>3
<b>X = </b>{1, 2, 1}
<b>Y = </b>{2, 3, 3}
<b>Output:</b>
2
<b>Explanation:</b>
The pairs {(1,2), (1,3)}, and {(1,3), (2,3)}
have equal Manhatten and Euclidean distance.</pre>

 

<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>numOfPairs()</b> which takes an Integer N and two arrays X, and Y of length N as input and returns the number of pairs with equal Manhattan and Euclidean Distance. (X[i], Y[i]) denotes a point.

 

<b>Expected Time Complexity:</b> O(N)<br>
<b>Expected Auxiliary Space:</b> O(N)

 

<b>Constraints:</b><br>
1 <= N <= 10<sup>5</sup><br>
 -10^9 <= X[i], Y[i] <= 10^9


<hr>

### Tags
- **Topic Tags:** `Hash` `Mathematical` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Pairs With Same Manhattan And Euclidean Distance](https://www.geeksforgeeks.org/pairs-with-same-manhattan-and-euclidean-distance/)
