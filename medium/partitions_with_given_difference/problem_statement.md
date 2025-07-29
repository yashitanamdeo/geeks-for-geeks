<h1 align="center">Partitions with Given Difference</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 36.76%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 193K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[]</b>, partition it into two subsets(possibly empty) such that each element must belong to only one subset. Let the sum of the elements of these two subsets be <b>sum1</b> and <b>sum</b><b>2</b>. Given a difference <b>d</b>, count the number of partitions in which <b>sum</b><b>1</b> is greater than or equal to <b>sum</b><b>2</b> and the difference between <b>sum</b><b>1</b> and <b>sum</b><b>2</b> is equal to <b>d</b>. 

<b>Examples :</b>

<pre><b>Input: </b>arr[] =  [5, 2, 6, 4], d = 3
<b>Output: </b>1
<b>Explanation: </b>There is only one possible partition of this array. Partition : {6, 4}, {5, 2}. The subset difference between subset sum is: (6 + 4) - (5 + 2) = 3.</pre>

<pre><b>Input:</b> arr[] = [1, 1, 1, 1], d = 0 <br><b>Output:</b> 6 <br><b>Explanation: </b>We can choose two 1's from indices {0,1}, {0,2}, {0,3}, {1,2}, {1,3}, {2,3} and put them in sum1 and remaning two 1's in sum2.<br>Thus there are total 6 ways for partition the array arr. <br></pre>

<pre><b>Input:</b> arr[] = [1, 2, 1, 0, 1, 3, 3], d = 11<br><b>Output:</b> 2</pre>

<b>Constraint:</b><br>1 <= arr.size() <= 50<br>0 <= d  <= 50<br>0 <= arr[i] <= 6

## Expected Complexities
- Time Complexity: O( n*sum(arr))
- Auxiliary Space: O( sum(arr))

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Arrays`
- **Company Tags:** `None`

### Related Articles
- [Count Of Subsets With Given Difference](https://www.geeksforgeeks.org/count-of-subsets-with-given-difference/)
