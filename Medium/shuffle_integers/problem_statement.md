<h1 align="center">Shuffle integers</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 36.88%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 56K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr</b> of <b>n </b>elements in the following format {a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, a<sub>4</sub>, ... , a<sub>n/2</sub>, b<sub>1</sub>, b<sub>2</sub>, b<sub>3</sub>, b<sub>4</sub>, ... , b<sub>n/2</sub>}, the task is shuffle the array to {a<sub>1</sub>, b<sub>1</sub>, a<sub>2</sub>, b<sub>2</sub>, a<sub>3</sub>, b<sub>3</sub>, ... , a<sub>n/2</sub>, b<sub>n/2</sub>} without using extra space.<br>Note that n is <b>even</b>.

<b>Example 1:</b>

<pre><b>Input: <br></b>n = 4, arr = {1, 2, 9, 15}
<b>Output:</b>  <br>1 9 2 15
<b>Explanation</b>: <br>a<sub>1</sub>=1, a<sub>2</sub>=2, b<sub>1</sub>=9, b<sub>2</sub>=15. So the final array will be: a<sub>1</sub>, b<sub>1</sub>, a<sub>2</sub>, b<sub>2</sub> = {1,9,2,15}.</pre>

<b>Example 2:</b><b><br></b>

<pre><b>Input: <br></b>n = 6 arr = {1, 2, 3, 4, 5, 6} <br><b>Output:</b> <br>1 4 2 5 3 6</pre>

<b>Your Task:</b><br>This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function <b>shuffleArray() </b>that takes array<b> arr, </b>and an integer<b> n</b> as parameters and modifies the given array according to the above-given pattern.

<b>Expected Time Complexity:</b> O(n).<br><b>Expected Auxiliary Space:</b> O(1).

<b>Constraints:</b><br>1 ≤ n ≤ 10<sup>5</sup><br>1 ≤ arr<sub>i </sub>≤ 10<sup>3</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Recursion` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon` `OYO Rooms`

### Related Articles
- [Shuffle Array A1 B1 A2 B2 A3 B3 Bn Without Using Extra Space](https://www.geeksforgeeks.org/shuffle-array-a1-b1-a2-b2-a3-b3-bn-without-using-extra-space/)
