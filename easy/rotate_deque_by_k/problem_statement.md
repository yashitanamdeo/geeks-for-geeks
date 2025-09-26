<h1 align="center">Rotate Deque By K</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 75.79%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 22K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a deque <b>dq </b>(double-ended queue) containing non-negative integers, along with two positive integer <b>type </b>and <b>k</b>. The task is to rotate the deque circularly by <b>k</b> positions.<br>There are two types of rotation operations:

 

 

- <b>Right Rotation (Clockwise)</b>: If <b>type = 1</b>, rotate the deque to the right. This means moving the last element to the front, and repeating the process k times.
- <b>Left Rotation (Anti-Clockwise)</b>: If <b>type = 2</b>, rotate the deque to the left. This means moving the first element to the back, and repeating the process k times.
<b>Examples:</b>

<pre><b>Input: </b>dq = [1, 2, 3, 4, 5, 6], type = 1, k = 2
<b>Output:</b> [5, 6, 1, 2, 3, 4] 
<b>Explanation:</b> The type is 1 and k is 2. So, we need to right rotate dequeue by 2 times.<br>In first right rotation we get [6, 1, 2, 3, 4, 5].<br>In second right rotation we get [5, 6, 1, 2, 3, 4].</pre>

<pre><b>Input:</b> dq = [10, 20, 30, 40, 50], type = 2, k = 3 
<b>Output:</b> [40, 50, 10, 20, 30] 
<b>Explanation:</b> The type is 2 and k is 3. So, we need to left rotate dequeue by 3 times.<br>In first left rotation we get [20, 30, 40, 50, 10]. <br>In second left rotation we get [30, 40, 50, 10, 20].<br>In third left rotation we get [40, 50, 10, 20, 30].</pre>

<b>Constraints:</b><br>1 ≤ dq.size() ≤ 10<sup>5 <br></sup>1 ≤ k ≤ 10<sup>5 <br></sup>1 ≤ type ≤ 2

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Data Structures` `Deque`
- **Company Tags:** `None`
