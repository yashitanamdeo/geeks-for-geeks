<h1 align="center">Make Array Elements Equal</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.65%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 36K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an integer <b>N</b>. Consider an array <b>arr </b>having <b>N</b> elements where <b>arr[i]</b> = <b>2*i+1</b>. (The array is 0-indexed)

You are allowed to perform the given operation on the array any number of times:

1) Select two indices <b>i</b> and <b>j </b>and increase <b>arr[i]</b> by 1 and decrease <b>arr[j]</b> by 1.

Your task is to find the minimum number of such operations required to make all the elements of the array equal.

<b>Example 1:</b>

<pre><b>Input:</b>
N = 3
<b>Output:</b>
2
<b>Explanation:</b>
Initially the array is {1, 3, 5}. If we perform
the operation once on the indices 0 and 2, the 
resulting array will be {2, 3, 4}. If we again 
perform the operation once on the indices 0
and 2, the resulting array will be {3, 3, 3}.
Hence, the minimum operations required is 2
in this case. </pre>

<b>Example 2:</b>

<pre><b>Input: </b>
N = 2
<b>Output:</b>
1
<b>Explanation: </b>
The array initially is {1, 3}. After performing 
an operation the array will be {2, 2}. Hence,
the answer is 1 in this case.</pre>

<b>Your Task:</b><br>
Complete the function <b>minOperations</b><b>() </b>which takes the integer <b>N </b>as the input parameter, and returns the minimum operations required to make all the array elements equal.

<b>Expected Time Complexity:</b> O(1)<br>
<b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>
1 ≤ N ≤ 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures` `Algorithms`
- **Company Tags:** `Expedia`

### Related Articles
- [Make Array Elements Equal By Increasing Or Decreasing The Elements By 1](https://www.geeksforgeeks.org/make-array-elements-equal-by-increasing-or-decreasing-the-elements-by-1/)

### Related Interview Experiences
- [Expedia Interview Experience For Internship 2020](https://www.geeksforgeeks.org/expedia-interview-experience-for-internship-2020/)
