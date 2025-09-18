<h1 align="center">Next Greater Element in Circular Array</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 56.97%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 65K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a circular integer array <b>arr[]</b>, the task is to determine the next greater element <b>(NGE)</b> for each element in the array.

The next greater element of an element <b>arr[i]</b> is the first element that is greater than <b>arr[i]</b> when traversing circularly. If no such element exists, return <b>-1</b> for that position.

<b>Note: </b>Since the array is circular, after reaching the last element, the search continues from the beginning until we have looked at all elements once.

<b>Examples: </b>

<pre><b>Input</b>: arr[] = [1, 3, 2, 4]
<b>Output</b>: [3, 4, 4, -1]
<b>Explanation</b>:<br>The next greater element for 1 is 3.
The next greater element for 3 is 4.
The next greater element for 2 is 4.
The next greater element for 4 does not exist, so return -1.</pre>

<pre><b>Input</b>: arr[] = [0, 2, 3, 1, 1]
<b>Output</b>: [2, 3, -1, 2, 2]
<b>Explanation:
</b>The next greater element for 0 is 2.
The next greater element for 2 is 3.
The next greater element for 3 does not exist, so return -1.
The next greater element for 1 is 2 (from circular traversal).
The next greater element for 1 is 2 (from circular traversal).</pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>5</sup><sup><br></sup>0 ≤ arr[i] ≤ 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Stack` `Data Structures`
- **Company Tags:** `Flipkart` `Amazon` `Microsoft`

### Related Articles
- [Find The Next Greater Element In A Circular Array](https://www.geeksforgeeks.org/find-the-next-greater-element-in-a-circular-array/)
- [Next Greater Element](https://www.geeksforgeeks.org/next-greater-element/)

### Related Interview Experiences
- [Flipkart Interview Experience For Sde Internship 2021](https://www.geeksforgeeks.org/flipkart-interview-experience-for-sde-internship-2021/)
