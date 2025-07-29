<h1 align="center">Subset Sum Problem</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 32.0%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 380K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of positive integers <b>arr[]</b> and a value <b>sum</b>, determine if there is a subset of <b>arr[]</b> with sum equal to given <b>sum</b>. 

<b>Examples:</b>

<pre><b>Input</b>: arr[] = [3, 34, 4, 12, 5, 2], sum = 9<br><b>Output:</b> true 
<b>Explanation</b>: Here there exists a subset with target sum = 9, 4+3+2 = 9.
</pre>

<pre><b>Input</b>: arr[] = [3, 34, 4, 12, 5, 2], sum = 30
<b>Output:</b> false
<b>Explanation</b>: There is no subset with target sum 30.</pre>

<pre><b>Input</b>: arr[] = [1, 2, 3], sum = 6
<b>Output:</b> true<br><b>Explanation</b>: The entire array can be taken as a subset, giving 1 + 2 + 3 = 6.</pre>

<b>Constraints:</b><br>1 <= arr.size() <= 200<br>1<= arr[i] <= 200<br>1<= sum <= 10<sup>4</sup>

## Expected Complexities
- Time Complexity: O(sum*n)
- Auxiliary Space: O(sum)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `Amazon` `Microsoft`

### Related Articles
- [Subset Sum Problem Dp 25](https://www.geeksforgeeks.org/subset-sum-problem-dp-25/)
- [Subset Sum Problem](https://www.geeksforgeeks.org/subset-sum-problem/)

### Related Interview Experiences
- [Amazon Interview Experience For Sde](https://www.geeksforgeeks.org/amazon-interview-experience-for-sde/)
