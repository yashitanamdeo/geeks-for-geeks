<h1 align="center">Find k-th smallest element in given n ranges</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.29%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 31K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given <b>n </b>ranges of the form [p, q] which denotes all the numbers in the range [p, p + 1, p + 2,...q].  Given another integer <b>q </b>denoting the number of queries. The task is to return the <b>k<sup>th</sup></b> smallest element for each query (assume k>1) after <b>combining</b> all the ranges.<br>In case the <b>k<sup>th</sup></b> smallest element doesn't exist return -1. 

<b>Example 1:</b>

<pre><b>Input:<br></b>n = 2, q = 3
range[] = {{1, 4}, {6, 8}}
queries[] = {2, 6, 10}
<b>Output: <br></b>2 7 -1
<b>Explanation:</b> <br>After combining the given ranges, 
the numbers become 1 2 3 4 6 7 8. As here 2nd 
element is 2, so we print 2. As 6th element is 
7, so we print 7 and as 10th element doesn't <br>exist, so weprint -1.</pre>

<b>Example 2:</b>

<pre><b>Input:<br></b>n = 2, q = 2
range[] = {{2, 6}, {5, 7}} 
queries[] = {5, 8}
<b>Output: <br></b>6 -1
<b>Explantion: <br></b>After combining the ranges, we'll take <b>Union</b> of <br>range= {2,3,4,5,6,7}, here  5th smallest number <br>will be 6 and 8th smallest number does not exists.</pre>

<b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>kthSmallestNum</b><b>()</b> which takes a n * 2 array denoting the ranges and an array denoting the queries.

<b>Expected Time Complexity:</b> O(nlogn+q*n)<br><b>Expected Auxiliary Space:</b> O(q)

<b>Constraints:</b><br>1 <= n <= 10<sup>3</sup><br>1 <= range[i][0] <= range[i][1] <= 2*10<sup>9</sup><br>1 <= q <= 500<br>1 <= queries[i] <= 2*10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Searching` `Sorting` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Find K Th Smallest Element In Given N Ranges](https://www.geeksforgeeks.org/find-k-th-smallest-element-in-given-n-ranges/)
