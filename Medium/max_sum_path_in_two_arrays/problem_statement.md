<h1 align="center">Max sum path in two arrays</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 30.9%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 78K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two <b>sorted</b> arrays of <b>distinct </b>integers <b>arr1</b> and <b>arr2</b>. Each array may have some elements in common with the other array. Find the <b>maximum sum of a path</b> from the beginning of any array to the end of any array. You can switch from one array to another array only at the common elements. 

<b>Note:</b>  When we switch from one array to other,  we need to consider the common element only once in the result.<br>

<b>Examples : </b>

<pre><b>Input: </b>arr1 = [2, 3, 7, 10, 12] , arr2 = [1, 5, 7, 8]
<b>Output: </b>35<b>
Explanation: </b>The path will be 1+5+7+10+12 = 35, where 1 and 5 come from arr2 and then 7 is common so we switch to arr1 and add 10 and 12.</pre>

<pre><b>Input: </b>arr1 = [1, 2, 3] , arr2[] = [3, 4, 5]
<b>Output: </b>15<b>
Explanation: </b>The path will be 1+2+3+4+5=15.</pre>

<pre><b>Expected Time Complexity: </b>O(m + n)<br><b>Expected Auxiliary Space:</b> O(1)</pre>

<b>Constraints:</b><br>1 <= arr1.size(), arr2.size() <= 10<sup>4</sup><br>1 <= arr1[i], arr2[i] <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures`
- **Company Tags:** `Amazon`

### Related Articles
- [Maximum Sum Path Across Two Arrays](https://www.geeksforgeeks.org/maximum-sum-path-across-two-arrays/)
