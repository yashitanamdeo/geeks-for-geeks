<h1 align="center">Swap Kth nodes from ends</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 35.5%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 62K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 45m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

A singly linked list and an integer of k are given. You need to swap the k<sup>th</sup> node from the beginning and the k<sup>th</sup> node from the end of the linked list. Swap the nodes through the links. Do not change the content of the nodes.

<b>Note: </b>The driver code will output <b>"true"</b> if you successfully swap the nodes.

<b>Examples:</b>

<pre><b>Input: </b>LinkedList: 1->2->3->4, k = 1
<b>Output: </b>true<b>
Explanation: </b>Here k = 1, hence after swapping the 1st node from the beginning and end the new list will be 4->2->3->1. </pre>

<pre><b>Input: </b>LinkedList: 1->2->3->4->5, k = 7
<b>Output: </b>true<b>
Explanation: </b>k > n. Swapping is invalid. Return the head node as it is.<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/701070/Web/Other/blobid1_1722511116.png" alt="" title="" width="395" height="138"/> </pre>

<b>Expected Time Complexity</b>: O(n)<br><b>Expected Auxillary Space:</b> O(1)

<b>Constraints:</b><br>1 <= number of nodes <= 10<sup>3<br></sup>1 <= node->data <= 10<sup>6<br></sup>1 <= k <= 10<sup>3</sup>


<hr>

### Tags
- **Topic Tags:** `Linked List` `Data Structures`
- **Company Tags:** `Morgan Stanley` `Amazon`

### Related Articles
- [Swap Kth Node From Beginning With Kth Node From End In A Linked List](https://www.geeksforgeeks.org/swap-kth-node-from-beginning-with-kth-node-from-end-in-a-linked-list/)
