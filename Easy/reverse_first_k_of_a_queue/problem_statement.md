<h1 align="center">Reverse first K of a Queue</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 81.28%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 151K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an integer<b> k </b>and a [queue](http://www.geeksforgeeks.org/queue-data-structure/) of integers, we need to reverse the order of the first<b> k</b> elements of the queue, leaving the other elements in the same relative order.

Only following standard operations are allowed on queue.

- enqueue(x) : Add an item x to rear of queue
- dequeue() : Remove an item from front of queue
- size() : Returns number of elements in queue.
- front() : Finds front item.<br>
<b>Note:</b> The above operations represent the general processings. In-built functions of the respective languages can be used to solve the problem.

"If the size of queue is smaller than the given k , then return the original queue."

<b>Examples:</b>

<pre><b>Input: </b>q<b> </b>= [1, 2, 3, 4, 5], k = 3<br><b>Output: </b>[3, 2, 1, 4, 5]<br><b>Explanation: </b>After reversing the first 3 elements from the given queue the resultant queue will be 3 2 1 4 5</pre>

<pre><b>Input: </b>q<b> </b>= [4, 3, 2, 1], k = 4<br><b>Output: </b>[1, 2, 3, 4] <br><b>Explanation: </b>After reversing the first 4 elements from the given queue the resultant queue will be 1 2 3 4 </pre>

<b>Constraints:<br></b>1<=q[i]<=10<sup>5<br></sup>1<=q.size()<=10<sup>5</sup><br>1<=k<=10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Stack` `Queue` `Data Structures`
- **Company Tags:** `Amazon`

### Related Articles
- [Reversing First K Elements Queue](https://www.geeksforgeeks.org/reversing-first-k-elements-queue/)
