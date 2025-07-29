<h1 align="center">Maximize the sum of selected numbers from a sorted array to make it empty</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 55.96%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 21K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a array of<b> N</b> numbers, we need to maximize the sum of selected numbers. At each step, you need to select a number A<sub>i</sub>, delete one occurrence of <b>A<sub>i</sub>-1 (if exists), and A<sub>i</sub></b> each from the array. Repeat these steps until the array gets empty. The problem is to maximize the sum of the selected numbers.

<b>Note:</b> Numbers need to be selected from maximum to minimum.

<b>Example 1:</b>

<pre><b>Input :</b> arr[ ] = {1, 2, 2, 2, 3, 4}
<b>Output :</b> 10
<b>Explanation:</b>
We select 4, so 4 and 3 are deleted leaving us with {1,2,2,2}.
Then we select 2, so 2 & 1 are deleted. We are left with{2,2}.
We select 2 in next two steps, thus the sum is 4+2+2+2=10.
</pre>

<br>
<b>Example 2:</b>

<pre><b>Input :</b> arr[ ] = {1, 2, 3} <b>
Output :</b>  4
<b>Explanation:</b> We select 3, so 3 and 2 are deleted leaving us with {1}. Then we select 1, 0 doesn't exist so we delete 1. thus the sum is 3+1=4.
</pre>

 

<b>Your Task:</b><br>
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function <b>maximizeSum()</b> that takes an array <b>(arr)</b>, sizeOfArray <b>(n),</b> and return the maximum sum of the selected numbers. The driver code takes care of the printing.

<b>Expected Time Complexity:</b> O(NlogN).<br>
<b>Expected Auxiliary Space:</b> O(N).

<br>
<b>Constraints:</b><br>
1 ≤ N ≤ 10<sup>5</sup><br>
1 ≤ A[i] ≤ 10<sup>5</sup><br>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Map` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Maximize Sum Selected Numbers Performing Following Operation](https://www.geeksforgeeks.org/maximize-sum-selected-numbers-performing-following-operation/)
