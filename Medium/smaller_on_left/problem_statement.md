<h1 align="center">Smaller on Left</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 22.61%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 46K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr</b>[ ] of <b>n</b> positive integers, the task is to find the greatest element on the left of every element in the array which is strictly smaller than itself, if this element does not exist for an index print <b>"-1".</b>

<b>Examples:</b>

<pre><b>Input: </b>n = 5, arr[] = [2, 3, 4, 5, 1]
<b>Output: </b>-1 2 3 4 -1
<b>Explanation:<br></b>Greatest element on the left of 3 smaller 
than itself is 2, for 4 it is 3 and for 5 
it is 1. Since 2 is the first element and 
no element on its left is present, so it's 
greatest smaller element will be -1 and for 
1 no element smaller than itself is present 
on its left, so it's greatest smaller element 
is -1.
</pre>

<pre><b>Input: </b>n = 3, arr[] = [1, 2, 3] <b>
Output: </b>-1 1 2 </pre>

<b>Constraints:</b><br>1 ≤ n ≤ 10<sup>6</sup><br>1 ≤ arr[i] ≤ 10<sup>8</sup>

## Expected Complexities
- Time Complexity: O(n log n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `set` `Arrays` `Hash` `Map` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Find The Nearest Smaller Numbers On Left Side In An Array](https://www.geeksforgeeks.org/find-the-nearest-smaller-numbers-on-left-side-in-an-array/)
