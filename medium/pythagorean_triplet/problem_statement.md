<h1 align="center">Pythagorean Triplet</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 24.77%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 246K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[]</b>, return true if there is a <b>triplet (a, b, c)</b> from the array (where a, b, and c are on different indexes) that satisfies <b>a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup></b>, otherwise return false.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [3, 2, 4, 6, 5]
<b>Output:</b> true
<b>Explanation:</b> a=3, b=4, and c=5 forms a pythagorean triplet.
</pre>

<pre><b>Input: </b>arr[] = [3, 8, 5]
<b>Output:</b> false
<b>Explanation:</b> No such triplet possible.</pre>

<pre><b>Input: </b>arr[] = [1, 1, 1]
<b>Output:</b> false</pre>

<b>Constraints:</b><br>1 <= arr.size() <= 10<sup>5</sup><br>1 <= arr[i] <= 10<sup>3</sup>

## Expected Complexities
- Time Complexity: O(n + max(arr[i])^2)
- Auxiliary Space: O(max(arr[i]))

<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures`
- **Company Tags:** `Amazon` `Adobe`

### Related Articles
- [Find Pythagorean Triplet In An Unsorted Array](https://www.geeksforgeeks.org/find-pythagorean-triplet-in-an-unsorted-array/)

### Related Interview Experiences
- [Adobe Interview Experience For 2020 Internship](https://www.geeksforgeeks.org/adobe-interview-experience-for-2020-internship/)
