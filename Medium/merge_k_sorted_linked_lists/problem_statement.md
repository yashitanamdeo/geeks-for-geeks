<h1 align="center">Merge K sorted linked lists</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 57.01%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 110K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 60m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[] </b>of <b>n</b> <b>sorted linked lists</b> of different sizes. The task is to <b>merge</b> them in such a way that after merging they will be a <b>single sorted</b> linked list, then <b>return </b>the<b> head</b> of the merged linked list.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [1 -> 2 -> 3, 4 -> 5, 5 -> 6, 7 -> 8]
<b>Output: </b>1 -> 2 -> 3 -> 4 -> 5 -> 5 -> 6 -> 7 -> 8<b>
Explanation:<br></b>The arr[] has 4 sorted linked list of size 3, 2, 2, 2.
1st list: 1 -> 2-> 3
2nd list: 4 -> 5
3rd list: 5 -> 6
4th list: 7 -> 8
The merged list will be:
 </pre>

<pre><b>Input: </b>arr[] = [1 -> 3, 8, 4 -> 5 -> 6]
<b>Output: </b>1 -> 3 -> 4 -> 5 -> 6 -> 8<b>
Explanation:<br></b>The arr[] has 3 sorted linked list of size 2, 3, 1.
1st list: 1 -> 3
2nd list: 8
3rd list: 4 -> 5 -> 6
The merged list will be:<br>
</pre>

<b>Constraints</b><br>1 <= total no. of nodes <= 10<sup>5</sup><sup><br></sup>1 <= node->data <= 10<sup>3</sup>

## Expected Complexities
- Time Complexity: O(n log n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Linked List` `Heap` `Data Structures`
- **Company Tags:** `VMWare` `Amazon` `Microsoft` `Oracle`

### Related Articles
- [Merge K Sorted Linked Lists](https://www.geeksforgeeks.org/merge-k-sorted-linked-lists/)

### Related Interview Experiences
- [Vmware Interview Set 1 For Mts 2 Position](https://www.geeksforgeeks.org/vmware-interview-set-1-for-mts-2-position/)
