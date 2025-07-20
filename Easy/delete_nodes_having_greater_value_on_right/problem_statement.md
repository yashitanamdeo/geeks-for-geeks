<h1 align="center">Delete nodes having greater value on right</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 35.51%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 148K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a singly linked list, remove all nodes that have a node with a greater value anywhere to their right in the list. Return the head of the modified linked list.

<b>Examples:</b>

<pre><b>Input:
</b>LinkedList = 12->15->10->11->5->6->2->3
<b>Output: </b>15->11->6->3<br><b>
Explanation: </b>Since, 12, 10, 5 and 2 are the elements which have greater elements on the following nodes. So, after deleting them, the linked list would like be 15, 11, 6, 3.
</pre>

<pre><b>Input:
</b>LinkedList = 10->20->30->40->50->60
<b>Output: </b>60<br><br><b>Explanation: </b>All the nodes except the last node has a greater value node on its right, so all the nodes except the last node must be removed.</pre>

<b>Constraints:</b><br>1 ≤ size of linked list ≤ 10<sup>6</sup><br>1 ≤ element of linked list ≤ 10<sup>6</sup><br><br><b>Note: Try to solve the problem without using any extra space.</b>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Linked List` `Data Structures`
- **Company Tags:** `Amazon`

### Related Articles
- [Delete Nodes Which Have A Greater Value On Right Side](https://www.geeksforgeeks.org/delete-nodes-which-have-a-greater-value-on-right-side/)
- [Given Only A Pointer To A Node To Be Deleted In A Singly Linked List How Do You Delete It](https://www.geeksforgeeks.org/given-only-a-pointer-to-a-node-to-be-deleted-in-a-singly-linked-list-how-do-you-delete-it/)
