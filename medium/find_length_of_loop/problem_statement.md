<h1 align="center">Find length of Loop</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 44.26%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 282K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given the <b>head </b>of a linked list, determine whether the list contains a <b>loop</b>. If a loop is present, return the<b> number of nodes</b> in the loop, otherwise return<b> 0</b>.

<b>Note: </b>Internally, pos(1 based index) is used to denote the position of the node that tail's next pointer is connected to. If pos = 0, it means the last node points to null, indicating there is no loop. Note that pos is not passed as a parameter.

<b>Examples:</b>

<pre><b>Input: </b>pos = 2,<br>   <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/904501/Web/Other/blobid0_1756186026.webp" alt="" title="" width="434" height="90"/><b>
Output: </b>4<b>
Explanation: </b>There exists a loop in the linked list and the length of the loop is 4.<br></pre>

<pre><b>Input: </b>pos = 3,<br>   <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/904501/Web/Other/blobid0_1756128118.webp" alt="" title="" width="478" height="99"/>
<b>Output:</b> 3
<b>Explanation: </b>The loop is from 19 to 10. So length of loop is 19 → 33 → 10 = 3.</pre>

<pre><b>Input: </b>pos = 0,<br>    <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/904501/Web/Other/blobid1_1756128178.webp" alt="" title="" width="512" height="68"/><br><b>Output: </b>0<b>
Explanation: </b>There is no loop.<br></pre>

<b>Constraints:</b><br>1 ≤ number of nodes ≤ 10<sup>5</sup><sup><br></sup>1 ≤ node->data ≤ 10<sup>4</sup><br>0 ≤ pos < number of nodes

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Linked List` `Data Structures`
- **Company Tags:** `Amazon` `Adobe` `Qualcomm`

### Related Articles
- [Find Length Of Loop In Linked List](https://www.geeksforgeeks.org/find-length-of-loop-in-linked-list/)

### Related Interview Experiences
- [Qualcomm Interview Experience Set 10 Campus](https://www.geeksforgeeks.org/qualcomm-interview-experience-set-10-campus/)
- [Adobe Interview Experience Set 48 Campus](https://www.geeksforgeeks.org/adobe-interview-experience-set-48-campus/)
