<h1 align="center">Peak element</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 38.86%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 581K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array <b>arr[] </b>where no two adjacent elements are same, find the <b>index </b>of a <b>peak </b>element. An element is considered to be a <b>peak</b> if it is greater than its adjacent elements (if they exist). 

If there are multiple peak elements, Return index of any one of them. The output will be <b>"true"</b> if the index returned by your function is correct; otherwise, it will be "<b>false"</b>.

<b>Note:</b> Consider the element <b>before </b>the <b>first </b>element and the element <b>after </b>the <b>last </b>element to be <b>negative infinity</b>.

<b>Examples :<br></b>

<pre><b>Input: </b>arr = [1, 2, 4, 5, 7, 8, 3]
<b>Output:</b> true
<b>Explanation: </b>arr[5] = 8 is a peak element because arr[4] < arr[5] > arr[6].</pre>

<pre><b>Input: </b>arr = [10, 20, 15, 2, 23, 90, 80]
<b>Output: </b>true<b>
Explanation: </b>Element 20 at index 1 is a peak since 10 < 20 > 15. Index 5 (value 90) is also a peak, but returning any one peak index is valid.</pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>6</sup><br>-2<sup>31</sup> ≤ arr[i] ≤ 2<sup>31</sup> - 1

## Expected Complexities
- Time Complexity: O(log n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Searching` `Data Structures` `Algorithms` `Binary Search`
- **Company Tags:** `Accolite` `Amazon` `Visa` `Adobe` `Google`

### Related Articles
- [Find A Peak In A Given Array](https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/)

### Related Interview Experiences
- [Amazon Interview Experience Set 257 Off Campus]( http://www.geeksforgeeks.org/amazon-interview-experience-set-257-off-campus/)
