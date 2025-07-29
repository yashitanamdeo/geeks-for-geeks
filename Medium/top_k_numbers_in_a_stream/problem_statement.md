<h1 align="center">Top k numbers in a stream</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 49.1%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 47K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given <b>N</b> numbers in an array, your task is to keep <b>at most </b>the <b>top K </b>numbers with respect to their <b>frequency</b>.

In other words, you have to iterate over the array, and <b>after each index</b>, determine the <b>top K most frequent numbers </b>until that iteration and store them in an array in <b>decreasing order of frequency</b>. An array will be formed for each iteration and stored in <b>an array of arrays</b>. If the total number of distinct elements is less than <b>K</b>, then keep all the distinct numbers in the array. If two numbers have <b>equal frequency</b>, place the <b>smaller number first </b>in the array.

<b>Example 1:</b>

<pre><b>Input:
</b>N=5, K=4
arr[] = {5, 2, 1, 3, 2} 
<b>Output:</b> <br>5 <br>2 5 <br>1 2 5 <br>1 2 3 5 <br>2 1 3 5 
<b>Explanation</b>:
Firstly there was 5 whose frequency
is max till now. So resulting sequence is {5}.
Then came 2, which is smaller than 5 but
their frequencies are same so resulting sequence is {2, 5}.<br>Then came 1, which is the smallest among all the
numbers arrived, so resulting sequence is {1, 2, 5}.<br>Then came 3 , so resulting sequence is {1, 2, 3, 5}<br>Then again 2, which has the highest
frequency among all numbers, <br>so resulting sequence {2, 1, 3, 5}.</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>N=6, K=3
arr[] = {2, 1, 2, 1, 2, 1} 
<b>Output:</b> <br>2 <br>1 2 <br>2 1 <br>1 2 <br>2 1<br>1 2<br><b>Explanation:<br></b>As total number of distinct values never<br>exceeds 2, you have to return only those two<br>values. In the case where frequency of 1 gets<br>equal with the frequency of 2, you have to <br>keep 1 before 2 in the array.</pre>

<b>Your Task:</b><br>Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function <b>kTop()</b> that takes <b>array a</b>, <b>integer n</b> <b>and integer k</b> as parameters and returns the array of arrays.

<b>Expected Time Complexity:</b> O(N*K).<br><b>Expected Auxiliary Space:</b> O(N).

<b>Constraints:</b><br>1 ≤ N ≤ 10<sup>4<br></sup>1 ≤ K ≤ 10<sup>2</sup><sup><br></sup>1 ≤ a[i] ≤ 10<sup>2</sup><sup> </sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Map` `priority-queue` `Data Structures`
- **Company Tags:** `Accolite` `Amazon` `Media.net`

### Related Articles
- [Find Top K Or Most Frequent Numbers In A Stream](https://www.geeksforgeeks.org/find-top-k-or-most-frequent-numbers-in-a-stream/)

### Related Interview Experiences
- [Amazon Interview Experience Set 228 On Campus For Internship]( http://www.geeksforgeeks.org/amazon-interview-experience-set-228-on-campus-for-internship/)
