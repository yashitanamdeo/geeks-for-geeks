<h1 align="center">Count Reverse Pairs</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.0%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 22K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array <b>arr[]</b> of positive<b> </b>integers, find the count of <b>reverse pairs</b>. A pair of indices (i, j) is said to be a <b>reverse pair</b> if both the following conditions are met:

- 0 ≤ i < j < arr.size()
- arr[i] > 2 * arr[j]
#### <b>Examples</b>:
<pre><b>Input</b>: arr[] = [3, 2, 4, 5, 1, 20]
<b>Output</b>: 3
<b>Explanation</b>:
The Reverse pairs are 
(0, 4), arr[0] = 3, arr[4] = 1, 3 > 2*1 
(2, 4), arr[2] = 4, arr[4] = 1, 4 > 2*1 
(3, 4), arr[3] = 5, arr[4] = 1, 5 > 2*1 
</pre>

<pre><b>Input</b>: arr[] = [5, 4, 3, 2, 2]
<b>Output</b>: 2
<b>Explanation</b>:<br>The Reverse pairs are
(0, 3), arr[0] = 5, arr[3] = 2, 5 > 2*2
(0, 4), arr[0] = 5, arr[4] = 2, 5 > 2*2</pre>

<b>Constraints:<br></b>1 ≤ arr.size() ≤ 5*10<sup>4</sup><br>1 ≤ arr[i] ≤ 10<sup>9</sup>

## Expected Complexities
- Time Complexity: O(n log n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Binary Search` `Segment-Tree` `Binary Indexed Tree` `Divide and Conquer` `Merge Sort` `Arrays`
- **Company Tags:** `Bloomberg` `Amazon` `Microsoft` `Adobe` `Google` `Uber`

### Related Articles
- [Find The Count Of Reverse Pairs](https://www.geeksforgeeks.org/find-the-count-of-reverse-pairs/)
