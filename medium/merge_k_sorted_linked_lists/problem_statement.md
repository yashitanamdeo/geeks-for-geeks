<h1 align="center">Merge K sorted linked lists</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 57.01%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 117K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 60m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[] </b>of <b>n</b> <b>sorted linked lists</b> of different sizes. Your task is to <b>merge </b>all these lists into a single <b>sorted</b> linked list and return the <b>head </b>of the merged list.

<b>Examples:</b>

<pre><b>Input:<br>   <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/908368/Web/Other/blobid0_1756363954.webp" alt="" title="" width="404" height="180"/></b>
<b>Output: </b>1 -> 2 -> 3 -> 4 -> 7 -> 8 -> 9<b>
Explanation: </b>The arr[] has 3 sorted linked list of size 3, 3, 1.<br>1st list: 1 -> 3 -> 7<br>2nd list: 2 -> 4 -> 8<br>3rd list: 9<br>The merged list will be: <br>    <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700265/Web/Other/blobid2_1756115425.jpg" alt="" title="" width="595" height="60"/></pre>

<pre><b>Input:<br>   <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700265/Web/Other/blobid3_1756115435.jpg" alt="" title="" width="385" height="147"/><br></b><b>Output: </b>1 -> 3 -> 4 -> 5 -> 6 -> 8<b><br></b><b>Explanation: </b>The arr[] has 3 sorted linked list of size 2, 1, 3.<br>1st list: 1 -> 3<br>2nd list: 8<br>3rd list: 4 -> 5 -> 6<br>The merged list will be: <br>    <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700265/Web/Other/blobid4_1756115445.jpg" alt="" title="" width="546" height="63"/></pre>

<b>Constraints</b><br>1 ≤ total no. of nodes ≤ 10<sup>5</sup><sup><br></sup>1 ≤ node->data ≤ 10<sup>3</sup>

## Expected Complexities
- Time Complexity: O(n log n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Linked List` `Heap` `Data Structures` `Merge Sort` `two-pointer-algorithm`
- **Company Tags:** `VMWare` `Amazon` `Microsoft` `Oracle`

### Related Articles
- [Merge K Sorted Linked Lists](https://www.geeksforgeeks.org/merge-k-sorted-linked-lists/)

### Related Interview Experiences
- [Vmware Interview Set 1 For Mts 2 Position](https://www.geeksforgeeks.org/vmware-interview-set-1-for-mts-2-position/)
