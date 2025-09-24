<h1 align="center">Design MinMax Queue</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 72.97%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 8K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Design a <b>SpecialQueue </b>data structure that functions like a normal queue but with additional support for retrieving the minimum and maximum element efficiently.<br>The SpecialQueue must support the following operations:

- <b>enqueue(x): </b>Insert an element x at the rear of the queue.
- <b>dequeue(): </b>Remove the element from the front of the queue.
- <b>getFront(): </b>Return the front element without removing.
- <b>getMin(): </b>Return the minimum element in the queue in O(1) time.
- <b>getMax(): </b>Return the maximum element in the queue in O(1) time.
There will be a sequence of queries <b>queries</b><b>[][]</b>. The queries are represented in numeric form:

- <b>1 x</b> <b>:</b> Call enqueue(x)
- <b>2</b><b>:</b>  Call dequeue()
- <b>3:</b> Call getFront()
- <b>4: </b>Call getMin()
- <b>5:</b> Call getMax()
The driver code will process the queries, call the corresponding functions, and print the outputs of getFront(), getMin(), getMax() operations.<br>You only need to implement the above five functions.

<b>Note: </b>It is guaranteed that all the queries are valid.

<b>Examples:</b>

<pre><b>Input: </b>q = 6, queries[][] = [[1, 4], [1, 2], [3], [4], [2], [5]]<b>
Output: </b>[4, 2, 2]<b>
Explanation: </b>Queries on queue are as follows:<br>enqueue(4): Insert 4 at the rear of the queue.
enqueue(2): Insert 2 at the rear of the queue.<br>return the front element i.e 4
return minimum element from the queue i.e 2<br>dequeue(): Remove the front element 4 from the queue
return maximum element from the queue i.e 2</pre>

<pre><b>Input:</b> q = 4, queries[][] = [[1, 3], [4], [1, 5], [5]]<b>
Output: </b>[3, 5]<b>
Explanation: </b>Queries on queue are as follows:<b><br></b>enqueue(3): Insert 3 at the rear of the queue.
return minimum element from the queue i.e 3<br>enqueue(5): Insert 5 at the rear of the queue.<br>return maximum element from the queue i.e 5</pre>

<b>Constraints:<br></b>1 ≤ queries.size() ≤ 10<sup>5<br></sup>0 ≤ values in the queue ≤ 10<sup>9</sup>

## Expected Complexities
- Time Complexity: O(1)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Deque` `implementation` `Data Structures` `Queue`
- **Company Tags:** `None`

### Related Articles
- [Design A Queue Data Structure To Get Minimum Or Maximum In O1 Time](https://www.geeksforgeeks.org/design-a-queue-data-structure-to-get-minimum-or-maximum-in-o1-time/)
