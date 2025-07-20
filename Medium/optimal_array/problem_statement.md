<h1 align="center">Optimal Array</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 69.73%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 18K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a <b>sorted</b> array <b>a</b> of length<b> n</b>. For each <b>i</b>(0<=i<=n-1), you have to make all the elements of the array from index 0 till i<b> equal</b>, using minimum number of operations. In one operation you either <b>increase </b>or <b>decrease</b> the array element by <b>1</b>.

You have to return a <b>list</b> which contains the <b>minimum</b> number of operations for each i, to accomplish the above task.

<b>Note:</b><br>
1. 0-based indexing.<br>
2. For each index, you need to consider the same array which was given to you at the start.

<b>Example 1:</b>

<pre><b>Input:</b>
N=4
A={1,6,9,12}

<b>Output:</b>
0 5 8 14

<b>Explanation:</b>
For i=0, We do not need to perform any 
operation, our array will be {1}->{1}.
And minimum number of operations
will be 0.

For i=1, We can choose to convert all 
the elements from 0<=j<=i to 4, our 
array will become {1,6}->{4,4}. And 
minimum number of operations will be 
|1-4|+|6-4|=5.

For i=2, We can choose to convert all 
the elements from 0<=j<=i to 6, our 
array will become {1,6,9}->{6,6,6} and 
the minimum number of operations will 
be |1-6|+|6-6|+|9-6|=8.

Similarly, for i=3, we can choose to 
convert all the elements to 8, 
{1,6,9,12}->{8,8,8,8}, and the 
minimum number of operations will be 14.</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N=7
A={1,1,1,7,7,10,19}

<b>Output:</b>
0 0 0 6 12 21 33

<b>Explanation:</b>
Possible operations could be:
{1}->{1}
{1,1}->{1,1}
{1,1,1}->{1,1,1}
{1,1,1,7}->{1,1,1,1}
{1,1,1,7,7}->{1,1,1,1,1}
{1,1,1,7,7,10}->{5,5,5,5,5,5}
{1,1,1,7,7,10,19}->{7,7,7,7,7,7,7}

</pre>

<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function optimalArray() which takes N(length of array) and  an array A as input and returns an array of size N  with optimal answer for each index i.

<b>Expected Time Complexity: O(N)<br>
Expected Auxiliary Space: O(1)</b>

<b>Constraints:</b><br>
1 <= N <= 10<sup>6</sup><br>
-10<sup>5</sup> <= A[i] <= 10<sup>5</sup><br>
Sum of N over all test case does not exceed 10<sup>6</sup>.


<hr>

### Tags
- **Topic Tags:** `Arrays` `Sorting` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Optimal Array](https://www.geeksforgeeks.org/optimal-array/)
