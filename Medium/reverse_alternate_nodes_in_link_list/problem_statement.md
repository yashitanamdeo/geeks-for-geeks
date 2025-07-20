<h1 align="center">Reverse alternate nodes in Link List</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 48.48%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 56K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 40m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a linked list, you have to perform the following task:

1. Extract the alternative nodes starting from the second node.
1. Reverse the extracted list.
1. Append the extracted list at the end of the original list.
<b>Note</b>: Try to solve the problem without using any extra memory.

<b>Examples:</b>

<pre><b>Input: </b>LinkedList: 10->4->9->1->3->5->9->4
<b>Output: </b>10->9->3->9->4->5->1->4<br><b>
Explanation: </b>Alternative nodes in the given linked list are 4,1,5,4. Reversing the alternative nodes from the given list, and then appending them to the end of the list results in a list 10->9->3->9->4->5->1->4.
</pre>

<pre><b>Input: </b>LinkedList: 1->2->3->4->5
<b>Output: </b>1->3->5->4->2 <br><b>
Explanation: </b>Alternative nodes in the given linked list are 2 and 4. Reversing the alternative nodes from the given list, and then appending them to the end of the list results in a list of 1->3->5->4->2.</pre>

<b>Expected Time Complexity:</b> O(n)<br><b>Expected Space </b><b>Complexity</b><b>:</b> O(1)

<b>Constraints:</b><br>1 <= size of linked list <= 10<sup>6</sup><br>0 <= Node_value <= 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Linked List` `Data Structures`
- **Company Tags:** `Amazon` `Walmart`

### Related Articles
- [Given Linked List Reverse Alternate Nodes Append End](https://www.geeksforgeeks.org/given-linked-list-reverse-alternate-nodes-append-end/)
