<h1 align="center">Game Of Subsets</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 66.87%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 19K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Elena is the topper of the class. Once her teacher asked her a problem. He gave Elena an array of integers of length <b>n</b>. He calls a subset of array <b>arr good</b> if its product can be represented as a product of one or more <b>distinct prime</b> numbers. He asked her to find the number of different <b>good</b> subsets in <b>arr</b> modulo 10<sup>9</sup> + 7.

As a good friend of Elena help her to solve the problem.

<b>Example 1:</b>

<pre><b>Input:
</b>N: 4
arr: {1,2,3,4}
<b>Output: 6</b>
<b>Explanation: </b>
The good subsets are:
- [1,2]: product is 2, which is the product of distinct
prime 2.
- [1,2,3]: product is 6, which is the product of 
distinct primes 2 and 3.
- [1,3]: product is 3, which is the product of distinct
prime 3.
- [2]: product is 2, which is the product of distinct
 prime 2.
- [2,3]: product is 6, which is the product of distinct
primes 2 and 3.
- [3]: product is 3, which is the product of distinct
prime 3.</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>N : 3
arr : {2, 2, 3}<b>
Output: 5</b><b>
Explanantion:
</b>The good subsets are : {2}, {2}, {2, 3}, {2, 3}, {3}</pre>

<b>Your Task:</b><br>
The task is to complete the function <b>goodSubsets</b>() which takes an integer<b> n</b> and an array <b>arr </b>as the input parameters and should return the number of different good subsets.

<b>Expected Time Complexity: </b>O(NlogN)<br>
<b>Expected Space Complexity: </b>O(N)

<b>Constraints:</b>

- 1 <= <b>N </b><= 10<sup>5</sup>
- 1< = <b>arr[i] </b><= 30


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Bit Magic` `Data Structures` `Algorithms`
- **Company Tags:** `None`
