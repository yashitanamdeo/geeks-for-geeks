<h1 align="center">Count Pairs whose sum is equal to X</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 39.61%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 110K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two linked lists <b>head</b><b>1</b><b> </b>and <b>head2</b> with <b>distinct </b>elements, determine the <b>count of all distinct pairs</b> from both lists whose sum equals the given value <b>x</b>.

<b>Note</b>: A valid pair would be in the form <b>(x, y) </b>where <b>x</b> is from the first linked list and <b>y</b> is from the second linked list. (1, 3) and (3, 1) are considered different.

<b>Examples:</b>

<pre><b>Input: </b>head1 = 1->2->3->4->5->6, head2 = 11->12->13, x = 15<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700607/Web/Other/blobid1_1725335639.png" alt="" title="" width="374" height="187"/>
<b>Output: </b>3<b>
Explanation: </b>There are total 3 pairs whose sum is 15 : (4,11) , (3,12) and (2,13)<br></pre>

<pre><b>Input: </b>head1 = 7->5->1->3, head2 = 3->5->2->8, x = 10<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700607/Web/Other/blobid2_1725335674.png" alt="" title="" width="366" height="183"/><br><b>Output: </b>2<b>
Explanation: </b>There are total 2 pairs whose sum is 10 : (7,3) and (5,5)</pre>

<b>Constraints:</b><br>1<= size of both LinkedList <=10<sup>6</sup><br>1 <= node->data <= 10<sup>9</sup><br>1<= x <= 10<sup>9<br></sup><b>Note</b>: All elements in each linked list are unique.

## Expected Complexities
- Time Complexity: O(length(head1) + length(head2))
- Auxiliary Space: O(length(head1)) or  O(length(head2))

<hr>

### Tags
- **Topic Tags:** `Linked List` `Data Structures`
- **Company Tags:** `Amazon`

### Related Articles
- [Count Pairs Two Linked Lists Whose Sum Equal Given Value](https://www.geeksforgeeks.org/count-pairs-two-linked-lists-whose-sum-equal-given-value/)
