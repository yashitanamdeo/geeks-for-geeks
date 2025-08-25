<h1 align="center">Maximize median after doing k addition operation</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 44.57%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 18K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[]</b> consisting of positive integers and an integer <b>k</b>. You are allowed to perform <b>at most k operations</b>, where in each operation, you can <b>increment </b>any one element of the array by<b> 1</b>. Determine the <b>maximum possible median</b> of the array that can be achieved after performing at most <b>k</b> such operations.<br>

<b>Note: </b>The median of an array is defined as the middle element when the array (after sorting) has an odd size, or the average of the two middle elements when the array (after sorting) has an even size.

<b>Examples:</b>

<pre><b>Input:</b> arr[] = [1, 3, 4, 5], k = 3<br><b>Output:</b> 5<br><b>Explanation:</b> We can add +2 to the second element and +1 to the third element to get the array [1, 5, 5, 5]. After sorting, the array remains [1, 5, 5, 5]. Since the length is even, the median is (5 + 5) / 2 = 5.<br></pre>

<pre><b>Input:</b> arr[] = [1, 3, 6, 4, 2], k = 10<br><b>Output:</b> 7<br><b>Explanation: </b>After applying operations optimally, we can transform the array to [1, 3, 7, 7, 7] (one possible way). Sorted array becomes [1, 3, 7, 7, 7]. Since the length is odd, the median is the middle element 7.</pre>

<b>Constraints:<br></b>1 ≤ arr.size() ≤ 10<sup>5</sup><br>0 ≤ arr[i], k ≤ 10<sup>9</sup><br>

## Expected Complexities
- Time Complexity: O(n * log k)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Binary Search` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Maximize Median After Doing K Addition Operation On The Array](https://www.geeksforgeeks.org/maximize-median-after-doing-k-addition-operation-on-the-array/)
