<h1 align="center">Sum of XOR of all pairs</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 45.14%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 52K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of <b>N</b> integers, find the <b>sum of xor </b>of all pairs of numbers in the array <b>arr</b>. In other words, select all possible pairs of <b>i</b> and <b>j</b> from <b>0</b> to <b>N-1 (i<j)</b> and determine <b>sum </b>of all <b>(arr<sub>i</sub> xor arr<sub>j</sub>)</b>.

<b>Example 1:</b>

<pre><b>Input :</b> arr[ ] = {7, 3, 5}
<b>Output :</b> 12
<b>Explanation:</b>
All possible pairs and there Xor
Value: ( 3 ^ 5 = 6 ) + (7 ^ 3 = 4)
 + ( 7 ^ 5 = 2 ) =  6 + 4 + 2 = 12
</pre>

<b>Example 2:</b>

<pre><b>Input :</b> arr[ ] = {5, 9, 7, 6} <b>
Output :</b>  47<br><b>Explanation:<br></b>All possible pairs and there Xor<br>Value: (5 ^ 9 = 12) + (5 ^ 7 = 2)<br> + (5 ^ 6 = 3) + (9 ^ 7 = 14)<br> + (9 ^ 6 = 15) + (7 ^ 6 = 1)<br> = 12 + 2 + 3 + 14 + 15 + 1 = 47</pre>

<b>Your Task:</b><br>You do not have to take input or print output. You only need to complete the function <b>sumXOR()</b> that takes an array <b>(arr)</b>, sizeOfArray <b>(n)</b>, and <b>return</b> the <b>sum of xor of all pairs </b>of numbers in the array.

<b>Expected Time Complexity:</b> O(n).<br><b>Expected Auxiliary Space:</b> O(1).

<b>Constraints</b><br>2 ≤ n ≤ 10<sup>5</sup><br>1 ≤ arr[i] ≤ 10<sup>5 </sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Bit Magic` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Sum Xor Pairs Array](https://www.geeksforgeeks.org/sum-xor-pairs-array/)
