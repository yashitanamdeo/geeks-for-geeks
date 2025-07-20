<h1 align="center">Max sum in the configuration</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 36.56%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 115K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an integer array <b>arr[]</b><b>. </b>Find the <b>maximum</b> value of the sum of<b> i*arr[i] </b>for all <b>0 </b><b>≤</b><b> i </b><b>≤</b><b> arr.size()-1</b>. The only operation allowed is to <b>rotate</b>(clockwise or counterclockwise) the array any number of times.

<b>Examples :</b>

<pre><b>Input: </b>arr[] = [8, 3, 1, 2]
<b>Output: </b>29<b>
Explanation: </b>Out of all the possible configurations by rotating the elements: arr[] = [3, 1, 2, 8] here (3*0) + (1*1) + (2*2) + (8*3) = 29 is maximum.<br></pre>

<pre><b>Input: </b>arr[] = [1, 2, 3]
<b>Output: </b>8<b>
Explanation: </b>Out of all the possible configurations by rotating the elements: arr[] = [1, 2, 3] here (1*0) + (2*1) + (3*2) = 8 is maximum.</pre>

<pre><b>Input: </b>arr[] = [4, 13]
<b>Output: </b>13</pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>4</sup><br>1 ≤ arr[i] ≤ 20

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures` `Mathematical`
- **Company Tags:** `Amazon`

### Related Articles
- [Maximum Sum Iarri Among Rotations Given Array](https://www.geeksforgeeks.org/maximum-sum-iarri-among-rotations-given-array/)
