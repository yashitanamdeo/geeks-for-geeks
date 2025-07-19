<h1 align="center">Decimal Equivalent of Binary Linked List</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 21.23%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 76K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a singly linked list. The link list represents a <b>binary number, </b>ie- it contains only 0s and 1s. Find its decimal equivalent. <br>The significance of the bits <b>decreases </b>with the increasing index in the linked list. An empty linked list is considered to represent the decimal value <b>0</b>. 

Since the answer can be very large, the <b>answer modulo 10<sup>9</sup>+7</b> should be returned.

<b>Examples:</b>

<pre><b>Input: </b>Linked List = 1 -> 1 -> 1 -> 0<br><br><b>Output: </b>14<b><br></b><b>Explanation: </b>1*2<sup>3</sup> + 1*2<sup>2</sup> + 1*2<sup>1</sup> + 0*2<sup>0</sup> =  8 + 4 + 2 + 0 = 14</pre>

<pre><b>Input: </b>Linked List: 0 -> 1 -> 1<br><b>Output: </b>3<br><b>Explanation: </b>0*2<sup>2</sup> + 1*2<sup>1</sup> + 1*2<sup>0</sup> =  1 + 2 + 0 = 3</pre>

<b>Expected Time Complexity:</b> O(n)<br><b>Expected Space </b><b>Complexity</b><b>:</b> O(1)

<b>Constraints:</b><br>0 <= size of linked lists <= 10<sup>6</sup><br>data of each node is either 0 or 1


<hr>

### Tags
- **Topic Tags:** `Linked List` `Data Structures`
- **Company Tags:** `Juniper Networks`

### Related Articles
- [Decimal Equivalent Of Binary Linked List](https://www.geeksforgeeks.org/decimal-equivalent-of-binary-linked-list/)
