<h1 align="center">Prime List</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.68%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 42K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given the head of a linked list. You have to replace all the values of the nodes with the nearest <b>prime</b> number. If more than one prime number exists at an equal distance, choose the <b>smallest</b> one. Return the <b>head</b> of the modified linked list.

<b>Examples :</b>

<pre><b>Input: </b>head =<b> </b>2 → 6 → 10
<b>Output: </b>2 → 5 → 11<br><br><b>Explanation: </b>The nearest prime of 2 is 2 itself. The nearest primes of 6 are 5 and 7, since 5 is smaller so, 5 will be chosen. The nearest prime of 10 is 11.</pre>

<pre><b>Input: </b>head =<b> </b>1 → 15 → 20
<b>Output: </b>2 → 13 → 19<br><br><b>Explanation: </b>The nearest prime of 1 is 2. The nearest primes of 15 are 13 and 17, since 13 is smaller so, 13 will be chosen. The nearest prime of 20 is 19.</pre>

<b>Constraints:</b><br>1 <= no. of Nodes <= 10<sup>4</sup><br>1 <= node.val <= 10<sup>4</sup>

## Expected Complexities
- Time Complexity: O(n * sqrt(node.val))
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Linked List` `Mathematical` `Prime Number` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Replace The Values Of The Nodes With The Nearest Prime Number](https://www.geeksforgeeks.org/replace-the-values-of-the-nodes-with-the-nearest-prime-number/)
