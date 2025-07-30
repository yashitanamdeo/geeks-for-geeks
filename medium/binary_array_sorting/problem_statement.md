<h1 align="center">Binary Array Sorting</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.94%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 127K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a binary array <b>arr[]</b>, where each element is either <b>0 </b>or <b>1</b>. Your task is to rearrange the array in increasing order in place (without using extra space). You do not need to return anything; simply modify the input array.

<b>Examples:</b>

<pre><b>Input</b>: arr[] = [1, 0, 1, 1, 0]
<b>Output</b>: [0, 0, 1, 1, 1]
<b>Explanation</b>: After arranging the elements in increasing order, elements will be as 0 0 1 1 1.</pre>

<pre><b>Input</b>: arr[] = [1, 0, 1, 1, 1, 1, 1, 0, 0, 0]
<b>Output</b>: [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
<b>Explanation</b>: After arranging the elements in increasing order, elements will be 0 0 0 0 1 1 1 1 1 1.</pre>

<pre><b>Input</b>: arr[] = [1, 1, 1, 1]
<b>Output</b>: [1, 1, 1, 1]
<b>Explanation</b>: Since the array already contains only 1s, no change is needed.</pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>6</sup><br><b>arr[i</b><b>]</b> ∈ {0,1} for all valid indices <b>i</b>.

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Sorting` `Arrays` `two-pointer-algorithm`
- **Company Tags:** `None`
