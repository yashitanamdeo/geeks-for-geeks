<h1 align="center">Delete without head pointer</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 78.57%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 216K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a node <b>del_node</b> of a Singly Linked List where you have to <b>delete</b> a <b>value </b>of the given node from the linked list but you are not given the <b>head</b> of the list.

By deleting the node value, we do not mean removing it from memory. We mean:

- The value of the given node should not exist in the linked list.
- The number of nodes in the linked list should decrease by one.
- All the values before & after the <b>del_node </b>node should be in the same order.
<b>Note: </b>

1. Multiple nodes can have the same values as the del_node, but you must only remove the node whose pointer del_node is given to you.
1. It is guaranteed that there exists a node with a value equal to the del_node value<b> </b>and it will <b>not be the last node</b> of the linked list.
<b>Examples:</b>

<pre><b>Input: </b>Linked List = 1 -> 2, del_node = 1
<b>Output: </b>2<b>
Explanation: </b>After deleting 1 from the linked list, we have remaining nodes as 2.<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700161/Web/Other/blobid0_1724435615.png" alt="" title="" width="398" height="159"/> </pre>

<pre><b>Input: </b>Linked List = 10 -> 20 -> 4 -> 30, del_node = 20
<b>Output: </b>10->4->30<b>
Explanation: </b>After deleting 20 from the linked list, we have remaining nodes as 10, 4, 30.<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700161/Web/Other/blobid1_1724435635.png" alt="" title="" width="390" height="156"/><br></pre>

<b>Constraints:</b><br>2 <= number of nodes <= 10<sup>6 </sup> <br>1 <= node->data <= 10<sup>6</sup><br>

## Expected Complexities
- Time Complexity: O(1)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Linked List` `Data Structures`
- **Company Tags:** `Amazon` `Microsoft` `Samsung` `Visa` `Goldman Sachs` `Kritikal Solutions`

### Related Articles
- [Delete A Node From Linked List Without Head Pointer](https://www.geeksforgeeks.org/delete-a-node-from-linked-list-without-head-pointer/)
- [Given Only A Pointer To A Node To Be Deleted In A Singly Linked List How Do You Delete It](https://www.geeksforgeeks.org/given-only-a-pointer-to-a-node-to-be-deleted-in-a-singly-linked-list-how-do-you-delete-it/)
