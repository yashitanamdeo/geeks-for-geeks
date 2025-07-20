<h1 align="center">Pairwise swap elements of a linked list</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 52.06%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 129K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a singly linked list. The task is to swap elements in the linked list pairwise. For example, if the input list is 1 2 3 4, the resulting list after swaps will be 2 1 4 3.<br><b><br>Note</b>: You need to swap the nodes, not only the data. If only data is swapped then the driver code will print -1.

<b>Examples:</b>

<pre><b>Input: </b>LinkedList: 1->2->2->4->5->6->7->8
<b>Output: </b>2->1->4->2->6->5->8->7<br><b>
Explanation: </b>After swapping each pair considering (1,2), (2, 4), (5, 6).. so on as pairs, we get 2, 1, 4, 2, 6, 5, 8, 7 as a new linked list.
</pre>

<pre><b>Input: </b>LinkedList: 1->3->4->7->9->10->1
<b>Output: </b>3->1->7->4->10->9->1<br><b>
Explanation: </b>After swapping each pair considering (1,3), (4, 7), (9, 10).. so on as pairs, we get 3, 1, 7, 4, 10, 9, 1 as a new linked list.</pre>

<b>Constraints:</b><br>1 ≤ size of linked list ≤ 10<sup>6<br></sup>1 ≤ elements of linked list ≤ 10<sup>6</sup><sup><br></sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Linked List` `Data Structures`
- **Company Tags:** `Moonfrog Labs` `Amazon` `Microsoft` `Intuit`

### Related Articles
- [Pairwise Swap Elements Of A Given Linked List](https://www.geeksforgeeks.org/pairwise-swap-elements-of-a-given-linked-list/)

### Related Interview Experiences
- [Intuit Interview Experience Set 12](https://www.geeksforgeeks.org/intuit-interview-experience-set-12/)
