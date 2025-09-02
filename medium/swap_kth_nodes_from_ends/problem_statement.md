<h1 align="center">Swap Kth nodes from ends</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 35.5%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 75K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 45m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given the <b>head</b> of a singly linked list and an integer <b>k</b>. <b>Swap</b> the k<sup>th</sup> node (1-based index) from the <b>beginning</b> and the k<sup>th</sup> node from the <b>end</b> of the linked list. Return the head of the final formed list and if it's <b>not possible</b> to swap the nodes return the <b>original</b> list.

<b>Examples:</b>

<pre><b>Input: </b>k = 1,<br>  <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/701070/Web/Other/blobid0_1755953423.webp" alt="" title="" width="542" height="72"/><br><b>Output: </b>5 -> 2 -> 3 -> 4 -> 1<b>
Explanation: </b>Here k = 1, hence after swapping the 1st node from the beginning and end the new list will be 5 -> 2 -> 3 -> 4 -> 1.<br>  <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/701070/Web/Other/blobid1_1755953433.webp" alt="" title="" width="541" height="71"/><br></pre>

<pre><b>Input: </b>k = 2,<br><b>  <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/701070/Web/Other/blobid2_1755953453.webp" alt="" title="" width="564" height="65"/><br></b><b>Output: </b>5 -> 9 -> 8 -> 5 -> 10 -> 3<b>
Explanation: </b>Here k = 2, hence after swapping the 2nd node from the beginning and end the new list will be 5 -> 9 -> 8 -> 5 -> 10 -> 3.<br>  <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/701070/Web/Other/blobid3_1755953462.webp" alt="" title="" width="564" height="65"/><br></pre>

<b>Constraints:</b><br>1 ≤ list size ≤ 10<sup>4<br></sup>1 ≤ node->data ≤ 10<sup>6<br></sup>1 ≤ k ≤ 10<sup>4</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Linked List` `Data Structures`
- **Company Tags:** `Morgan Stanley` `Amazon`

### Related Articles
- [Swap Kth Node From Beginning With Kth Node From End In A Linked List](https://www.geeksforgeeks.org/swap-kth-node-from-beginning-with-kth-node-from-end-in-a-linked-list/)
