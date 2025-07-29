<h1 align="center">Adding Ones</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 48.06%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 48K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You start with an array <b>A</b> of size <b>N</b>. Initially all elements of the array A are <b>zero</b>. You will be given <b>K</b> positive integers. Let <b>j</b> be one of these integers, you have to add <b>1</b> to all <b>A[i]</b>, where <b>i ≥ j</b>. Your task is to print the array A after all these <b>K</b> updates are done. <br><b><br>Note:</b> Indices in updates array are given in 1-based indexing. That is updates[i] are in range [1,N].

<b>Example 1: </b>

<pre><b>Input:</b>
N = 3, K = 4
1 1 2 3
<b>Output:</b>
2 3 4
<b>Explanation:</b>
Initially the array is {0, 0, 0}. After the
first 1, it becomes {1, 1, 1}. After the
second 1 it becomes {2, 2, 2}. After 2, <br>it becomes {2, 3, 3} and <br>After 3 it becomes, {2, 3, 4}. </pre>

<b>Example 2: </b>

<pre><b>Input:</b>
N = 2, K = 3
1 1 1
<b>Output:</b>
3 3 
<b>Explanation:</b>
Initially the array is {0, 0}. After the
first 1, it becomes {1, 1}. After the
second 1 it becomes {2, 2}. After the
third 1, it becomes {3, 3}.</pre>

<b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>update()</b> which takes the array <b>A[]</b> and its size <b>N</b><b> </b>as inputs and make the updates and fill the array <b>A[].</b>

<b>Expected Time Complexity: </b>O(K)<br><b>Expected Auxiliary Space: </b>O(1)

<b>Constraints:</b><br>1 ≤ N, K ≤ 10<sup>5<br></sup>1<sup> </sup>≤ updates[i] ≤ N, for all i from 1 to K.


<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Prefix Sum Array Implementation Applications Competitive Programming](https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/)
