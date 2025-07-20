<h1 align="center">Reverse both parts</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 75.69%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 21K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a linked list and a number <b>k</b>. You have to reverse the first part of the linked list with k nodes and the second part with n-k nodes.

<b>Examples:</b>

<pre><b>Input: Linked list: </b>1 -> 2 -> 3 -> 4 -> 5,  k = 2<b>
Output: </b>2 -> 1 -> 5 -> 4 -> 3<br><b>
Explanation: </b>As k = 2 , so the first part 2 nodes: 1 -> 2 and the second part with 3 nodes: 3 -> 4 -> 5. Now after reversing the first part: 2 -> 1 and the second part: 5 -> 4 -> 3. So the output is: 2 -> 1 -> 5 -> 4 -> 3</pre>

<pre><b>Input: Linked list: </b>1 -> 2 -> 4 -> 3,  k = 3
<b>Output: </b>4 -> 2 -> 1 -> 3<br><br><b>Explanation: </b>As k = 3 , so the first part 3 nodes: 4 -> 2 -> 1 and the second part with 1 nodes: 3. Now after reversing the first part: 1 -> 2 -> 4 and the second part: 3. So the output is: 1 -> 2 -> 4 -> 3
</pre>

<b>Expected Time Complexity: </b>O(n)<b><br>Expected Space Complexity: </b>O(1)

<b>Constraints:</b><br>1 <= size of linked list <= 10<sup>6</sup>   <sup><br></sup>1 <= node->data <= 10<sup>6</sup><sup><br></sup>1 <= k < size of linked list


<hr>

### Tags
- **Topic Tags:** `Linked List` `Data Structures`
- **Company Tags:** `None`
