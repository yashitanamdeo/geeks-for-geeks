<h1 align="center">Allocate Minimum Pages</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 35.51%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 322K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 35m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[] </b>of integers, where each element <b>arr[i]</b> represents the number of pages in the i-th book. You also have an integer <b>k</b> representing the number of students. The task is to allocate books to each student such that:

- Each student receives atleast one book.
- Each student is assigned a contiguous sequence of books.
- No book is assigned to more than one student.
The objective is to <b>minimize the maximum number of pages </b>assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the <b>smallest possible maximum</b>.

<b>Note:</b> If it is not possible to allocate books to all students, return <b>-1</b>.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [12, 34, 67, 90], k = 2
<b>Output: </b>113
<b>Explanation: </b>Allocation can be done in following ways:<br>=> [12] and [34, 67, 90] Maximum Pages = 191<br>=> [12, 34] and [67, 90] Maximum Pages = 157<br>=> [12, 34, 67] and [90] Maximum Pages = 113.<br>The third combination has the minimum pages assigned to a student which is 113.</pre>

<pre><b>Input:</b> arr[] = [15, 17, 20], k = 5<br><b>Output: </b>-1<br><b>Explanation: </b>Since there are more students than total books, it's impossible to allocate a book to each student.</pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>6</sup><br>1 ≤ arr[i], k ≤ 10<sup>3</sup>

## Expected Complexities
- Time Complexity: O( n × log(sum(arr)))
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Searching` `Divide and Conquer` `Algorithms`
- **Company Tags:** `Infosys` `Amazon` `Microsoft` `Google` `Codenation` `Uber`

### Related Articles
- [Allocate Minimum Number Pages](https://www.geeksforgeeks.org/allocate-minimum-number-pages/)

### Related Interview Experiences
- [Amazon Interview Experience On Campus For Sde 1 5](https://www.geeksforgeeks.org/amazon-interview-experience-on-campus-for-sde-1-5/)
