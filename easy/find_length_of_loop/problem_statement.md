<h1 align="center">Find length of Loop</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 44.26%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 268K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given the head of a linked list, determine whether the list contains a loop. If a loop is present, <b>return the number of nodes</b> in the loop, otherwise <b>return 0</b>.

<b>Note: '</b>c<b>' </b>is the position of the node which is the next pointer of the last node of the linkedlist. If c is 0, then there is no loop.

<b>Examples:</b>

<pre><b>Input: </b>head: 1 → 2 → 3 → 4 → 5, c = 2<b>
Output: </b>4<b>
Explanation: </b>There exists a loop in the linked list and the length of the loop is 4.<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/893387/Web/Other/blobid0_1745983361.jpg" alt="" title="" width="340" height="182"/><br></pre>

<pre><b>Input: </b>head: 25 → 14 → 19 → 33 → 10 → 21 → 39 → 90 → 58 → 45, c = 4
<b>Output: </b>7<b>
Explanation: </b>The loop is from 33 to 45. So length of loop is 33 → <i>10 </i>→ 21 → 39 → 90 → 58 → <i>45</i> = 7.<br>The number 33 is connected to the last node of the linkedlist to form the loop because according to the input the 4<sup>th</sup> node from the beginning(1 based indexing) <br>will be connected to the last node in the LinkedList.<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/893387/Web/Other/blobid0_1745659828.jpg" alt="" title="" width="574" height="146"/><br></pre>

<pre><b>Input: </b>head: 0 → 1 → 2 → 3, c = 0
<b>Output: </b>0<b>
Explanation: </b>There is no loop.<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/893387/Web/Other/blobid1_1745662178.jpg" alt="" title="" width="506" height="105"/><br></pre>

<b>Constraints:</b><br>1 ≤ no. of nodes ≤ 10<sup>6<br></sup>0 ≤ node.data ≤ 10<sup>6</sup><br>0 ≤ c ≤ n-1

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
