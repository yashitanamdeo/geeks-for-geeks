<h1 align="center">At Least K Occurrences</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 37.11%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 207K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr</b>. Return the element that occurs at least<b> k</b> number of times.

<i>Note:</i>

- <b>If there are multiple answers, please return the first one.</b>
- <b>If there is no element found, return -1.</b>
<b>Examples</b>

<pre><b>Input: </b>arr[] = [1, 7, 4, 3, 4, 8, 7], k = 2
<b>Output: </b>4
<b>Explanation: </b>Both 7 and 4 occur 2 times. But 4 is first that occurs twice. As the index = 4, is the first element.</pre>

<pre><b>Input: </b> arr[] = [3, 1, 3, 4, 5, 1, 3, 3, 5, 4], k = 3<br><b>Output: </b>3<br><b>Explanation: </b>Here, 3 is the only number that appeared atleast 3 times in the array.<br></pre>

<pre><b>Input: </b>arr[] = [10, 8, 2], k = 10<br><b>Output: </b>-1<br><b>Explanation:</b> Here no element is returning atleast 10 number of times, so -1.</pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>6</sup><br>1 ≤ k ≤ 10<sup>3</sup><br>0 ≤ arr[i] ≤ 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Hash` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Count All Elements In The Array Which Appears At Least K Times After Their First Occurrence](https://www.geeksforgeeks.org/count-all-elements-in-the-array-which-appears-at-least-k-times-after-their-first-occurrence/)
