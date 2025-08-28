<h1 align="center">Maximize Number of 1's</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 39.46%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 69K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary array <b>arr[]</b> containing only 0s and 1s and an integer <b>k</b>, you are allowed to flip at most <b>k</b> 0s to 1s. Find the <b>maximum</b> number of consecutive <b>1's</b> that can be obtained in the array after performing the operation at most <b>k</b> times.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [1, 0, 1], k = 1
<b>Output: </b>3
<b>Explanation: </b>By flipping the zero at index 1, we get the longest subarray from index 0 to 2 containing all 1’s.</pre>

<pre><b>Input: </b>arr[] = [1, 0, 0, 1, 0, 1, 0, 1], k = 2
<b>Output: </b>5
<b>Explanation: </b>By flipping the zeroes at indices 4 and 6, we get the longest subarray from index 3 to 7 containing all 1’s.
</pre>

<pre><b>Input: </b>arr[] = [1, 1], k = 2
<b>Output: </b>2
<b>Explanation: </b>Since the array is already having the max consecutive 1's, hence we dont need to perform any operation. Hence the answer is 2.</pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>5</sup><br>0 ≤ k ≤ arr.size()<br>0 ≤ arr[i] ≤ 1

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures` `Binary Search` `sliding-window` `two-pointer-algorithm`
- **Company Tags:** `Accolite` `Amazon` `Microsoft` `MakeMyTrip`

### Related Articles
- [Find Zeroes To Be Flipped So That Number Of Consecutive 1s Is Maximized](https://www.geeksforgeeks.org/find-zeroes-to-be-flipped-so-that-number-of-consecutive-1s-is-maximized/)

### Related Interview Experiences
- [Accolite Interview Experience Set 11 On Campus](https://www.geeksforgeeks.org/accolite-interview-experience-set-11-on-campus/)
- [Amazon Interview Experience Set 388 Campus Full Time](https://www.geeksforgeeks.org/amazon-interview-experience-set-388-campus-full-time/)
- [Makemytrip Interview Experience For Sde On Campus](https://www.geeksforgeeks.org/makemytrip-interview-experience-for-sde-on-campus/)
