<h1 align="center">Sort by Set Bit Count</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 36.7%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 52K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of integers, sort the array (in descending order) according to count of set bits in binary representation of array elements.  

<b>Note:</b> For integers having same number of set bits in their binary representation, sort according to their position in the original array i.e., a stable sort.

 
<b>Example 1:</b>
<pre><b>Input: </b>
arr[] = {5, 2, 3, 9, 4, 6, 7, 15, 32};
<b>Output:</b>
15 7 5 3 9 6 2 4 32
<b>Explanation:</b>
The integers in their binary
representation are:
15 - 1111
7  - 0111
5  - 0101
3  - 0011
9  - 1001
6  - 0110
2  - 0010
4  - 0100
32 - 10000
hence the non-increasing sorted order is:
{15}, {7}, {5, 3, 9, 6}, {2, 4, 32}</pre>

 
<b>Example 2:</b>
<pre><b>Input: 
</b>arr[] = {1, 2, 3, 4, 5, 6};
<b>Output:</b> 
3 5 6 1 2 4
<b>Explanation:</b>
3  - 0011
5  - 0101
6  - 0110
1  - 0001
2  - 0010
4  - 0100
hence the non-increasing sorted order is
{3, 5, 6}, {1, 2, 4}</pre>

<br>
<br>
<b>Your Task:</b><br>
You don't need to print anything, printing is done by the driver code itself. You just need to complete the function <b>sortBySetBitCount() </b>which takes the array <b>arr[]</b> and its size <b>N</b><b> </b>as inputs and sort the array <b>arr[]</b> inplace. Use of extra space is prohibited.<br>
 

<b>Expected Time Complexity: </b>O(N.log(N))<br>
<b>Expected Auxiliary Space: </b>O(1)

<br>
<b>Constraints:</b><br>
1 ≤ N ≤ 10<sup>5</sup><br>
1 ≤ A[i] ≤ 10<sup>6</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Sorting` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Sort Array According Count Set Bits](https://www.geeksforgeeks.org/sort-array-according-count-set-bits/)
