<h1 align="center">Subarrays Product Less than K</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 21.0%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 109K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of positive numbers, the task is to find the number of possible contiguous subarrays having product less than a given number k. 

<b>Example 1:</b>

<pre><b>Input : 
</b>n = 4, k = 10
a[] = [1, 2, 3, 4]
<b>Output : </b>
7
<b>Explanation:</b>
The contiguous subarrays are {1}, {2}, {3}, {4} 
{1, 2}, {1, 2, 3} and {2, 3}, in all these subarrays<br>product of elements is less than 10, count of<br>such subarray is 7.<br>{2,3,4} will not be a valid subarray, because <br>2*3*4=24 which is greater than 10.</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>n = 7 , k = 100
a[] = [1, 9, 2, 8, 6, 4, 3]
<b>Output:</b>
16</pre>

<b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>countSubArrayProductLessThanK()</b> which takes the array <b>a[]</b>, its size <b>n</b><b> </b>and an integer <b>k</b> as inputs and returns the count of required subarrays.

<b>Constraints:</b><br>1<=n<=10<sup>6</sup><br>1<=k<=10<sup>15</sup><br>1<=a[i]<=10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures` `Algorithms` `sliding-window`
- **Company Tags:** `Goldman Sachs` `Facebook` `Walmart` `Yatra.com` `Amazon` `Linkedin` `Microsoft` `Uber`

### Related Articles
- [Number Subarrays Product Less K](https://www.geeksforgeeks.org/number-subarrays-product-less-k/)

### Related Interview Experiences
- [Goldman Sachs Interview Experience Set 32 Campus](https://www.geeksforgeeks.org/goldman-sachs-interview-experience-set-32-campus/)
