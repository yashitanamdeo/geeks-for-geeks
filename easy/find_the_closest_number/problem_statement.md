<h1 align="center">Find the closest number</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 27.1%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 87K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a <b>sorted</b> array <b>arr[]</b> of positive integers. The task is to find the closest value in the array to the given number <b>k</b>. The array may contain duplicate values.<br>Note: If the difference with k is the same for two values in the array return the greater value.<br>

<b>Examples :</b>

<pre><b>Input:</b>  arr[] = [1, 3, 6, 7], k = 4
<b>Output:</b> 3
<b>Explanation: </b>We have array arr={1, 3, 6, 7} and target is 4. If we look at the absolute difference of target with every element of the array we will get { |1-4|, |3-4|, |6-4|, |7-4| }  = {3, 1, 2, 3}. So, the closest number is <b>3.</b>
</pre>

<pre><b>Input: </b>arr[] = [1, 2, 3, 5, 6, 8, 9], k = 4
<b>Output: </b>5<br><b>Explanation: </b>The absolute difference of 4 is 1 from both 3 and 5. According to the question, we have to return greater value, which is 5.<br></pre>

<pre><b>Input: </b>arr[] = [6, 8, 8, 8, 9, 11, 13, 13, 15, 18, 19], k = 10
<b>Output: </b>11</pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>6</sup><br>1 ≤ k ≤ 10<sup>9</sup><br>1 ≤ arr[i] ≤ 10<sup>9</sup>

## Expected Complexities
- Time Complexity: O(log n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Algorithms` `Arrays` `Binary Search` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Find Closest Number Array](https://www.geeksforgeeks.org/find-closest-number-array/)
