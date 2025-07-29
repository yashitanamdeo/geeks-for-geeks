<h1 align="center">Flip Bits</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 23.15%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 61K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>A[]</b> consisting of <b>0’s</b> and <b>1’s</b>. A flip operation is one in which you turn <b>1</b> into <b>0</b> and a <b>0</b> into <b>1</b>. You have to do at most one “Flip” operation of any subarray. Formally, select a range <b>(l, r) </b>in the array <b>A[]</b>, such that (0 ≤ l ≤ r < n) holds and flip the elements in this range to get the maximum ones in the final array. You can possibly make zero operations to get the answer. You are asked to return the <b>maximum</b> number of 1 you can get in the array after doing flip operation.

<b>Example 1:</b>

<pre><b>Input:</b>
N = 5
A[] = {1, 0, 0, 1, 0} 
<b>Output:</b>
4
<b>Explanation:</b>
We can perform a flip operation in the range [1,2]
After flip operation array is : [<i> 1</i> <b>1 1</b> <i>1 0</i> ]
Count of one after fliping is : 4
<i>[Note: the subarray marked in bold is the flipped subarray]</i></pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N = 7
A[] = {1, 0, 0, 1, 0, 0, 1}
<b>Output:</b>
6
<b>Explanation:</b>
We can perform a flip operation in the range [1,5]
After flip operation array is : [<i> 1</i> <b>1 1 0 1 1</b> <i>1</i>]
Count of one after fliping is : 6
<i>[Note: the subarray marked in bold is the flipped subarray]</i></pre>

<b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>maxOnes()</b> which takes the array <b>A[]</b> and its size <b>N</b><b> </b>as inputs and returns the maximum number of 1's you can have in the array after atmost one flip operation.

<b>Expected Time Complexity:</b> O(N)<br><b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>1 ≤ N ≤ 10<sup>6</sup><br>0 ≤ A[i] ≤ 1


<hr>

### Tags
- **Topic Tags:** `Arrays` `Bit Magic` `Data Structures`
- **Company Tags:** `Amazon`

### Related Articles
- [Maximize Number 0s Flipping Subarray](https://www.geeksforgeeks.org/maximize-number-0s-flipping-subarray/)
