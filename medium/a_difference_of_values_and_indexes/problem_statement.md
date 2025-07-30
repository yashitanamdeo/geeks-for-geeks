<h1 align="center">A difference of values and indexes</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.02%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 21K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an unsorted array <b>arr[ ]</b> of size <b>n</b>, you need to find the maximum difference of absolute values of elements and indexes, i.e., for <b>i <= j</b>, calculate maximum of <b>| arr[ i ] - arr[ j ] | + | i - j |.</b> 

<b>Example 1:</b>

<pre><b>Input :</b> 
n = 3
arr[ ] = {1, 3, -1}
<b>Output:</b> 5
<b>Explanation:</b>
Maximum difference comes from indexes 
1, 2 i.e | 3 - (-1) | + | 1 - 2 | = 5
</pre>

<br>
<b>Example 2:</b>

<pre><b>Input :</b> 
n = 4
arr[ ] = {5, 9, 2, 6} <b>
Output:</b>  8
<b>Explanation:</b> 
Maximum difference comes from indexes 
1, 2 i.e | 9 - 2 | + | 1 - 2 | = 8
</pre>

 

<b>Your Task:</b><br>
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function <b>maxDistance()</b> that takes an array <b>(arr)</b>, sizeOfArray <b>(n)</b>, and return the maximum difference as given in the question.  The driver code takes care of the printing.

<b>Expected Time Complexity:</b> O(n).<br>
<b>Expected Auxiliary Space:</b> O(1).<br>
 

<b>Constraints:</b><br>
1 <= n <= 5*(10^5)<br>
-10^6 <= <b>arr[ i ]</b> <= 10^6


<hr>

### Tags
- **Topic Tags:** `Arrays` `Mathematical` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Maximum Absolute Difference Value Index Sums](https://www.geeksforgeeks.org/maximum-absolute-difference-value-index-sums/)
