<h1 align="center">Frequency in Queue</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 77.76%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 40K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

The task is to write two functions for a queue, <b>enqueue(k)</b> and <b>findFrequency(k)</b>. The first function inserts a given item <b>k</b> and the second function finds frequency of a given item <b>k</b>.

Every test case has <b>two arrays. </b>The first arrays is, insert[] which contains elements to be inserted in the queue. The second array is findFreq[] which contains items whose frequencies need to be found out.<br><b>Note:</b>

- enqueue(k) will be called for every element k in insert[].
- findFrequency(k) will be called for every element k in findFreq[];
<b>Examples:</b>

<pre><b>Input: </b>insert[] = 1 2 3 4 5 2 3 1 , findFreq[] = 1 3 2 9 10
<b>Output: </b>2 2 2 -1 -1
<b>Explanation:
</b>After inserting 1, 2, 3, 4, 5, 2, 3 and 1 into the queue, frequency of 1 is 2, 3 is 2 and 2 is 2.<br>Since 9 and 10 are not there in the queue we output -1 for them.</pre>

<pre><b>Input: </b>insert[] = 1 2 1 1 1 4 , findFreq[] = 1 5 4 3
<b>Output: </b>4 -1 1 -1
<b>Explanation:
</b>After inserting 1, 2, 1, 1, 1 and 4 into the queue, frequency of 1 is 4 and that of 4 is 1. <br>Since 5 and 3 are not there in the queue we output -1 for them.</pre>

<b>Constraints:</b><br>1 <= n <= 10<sup>3</sup><br>1 <= m <= 10<sup>3</sup><br>1 <= Elements of Queue <= 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(n * m)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Queue` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Queue Data Structure](https://www.geeksforgeeks.org/queue-data-structure/)
- [Queue Operations](https://www.geeksforgeeks.org/queue-operations/)
