<h1 align="center">Count the Coprimes</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 49.35%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 14K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array arr[] of positive integers. Your task is to count the number of pairs (i, j) such that:

 

- 0 ≤ i < j ≤ n-1
- gcd(arr[i], arr[j]) = 1
In other words, count the number of <b>unordered pairs</b> of indices (i, j) where the elements at those positions are <b>co-prime</b>.

<b>Examples:<br></b>

<pre><b>Input: </b>arr[] = [1, 2, 3]<b><br>Output: </b>3<b><br>Explanation: </b>(0,1), (0,2), (1,2) are the pair of indices where gcd(arr[i], arr[j]) = 1<b><br></b></pre>

<pre><b>Input:</b> arr[] = [4, 8, 3, 9]<b><br>Output: </b>4<b><br>Explanation: </b>(0,2), (0,3), (1,2), (1,3) are the pair of indices where gcd(arr[i], arr[j]) = 1<br></pre>

<b>Constraints:<br></b>2 ≤ arr.size() ≤ 10<sup>4</sup><b><br></b>1 ≤ arr[i] ≤ 10<sup>4</sup>

## Expected Complexities
- Time Complexity: O(n + M*log M), where M = max(arr[i])
- Auxiliary Space: O(M), where M = max(arr[i])

<hr>

### Tags
- **Topic Tags:** `number-theory` `Mathematical` `sieve` `inclusion-exclusion` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Find Number Co Prime Pairs Array](https://www.geeksforgeeks.org/find-number-co-prime-pairs-array/)
