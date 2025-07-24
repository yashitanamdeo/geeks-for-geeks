<h1 align="center">Smallest greater elements in whole array</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 39.0%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 25K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>A</b> of <b>N</b> length. We need to calculate the next smallest greater element for each element in a given array. If the next greater element is not available in a given array then we need to fill <b>-10000000</b> at that index place.

<b>Example 1:</b>

<pre><b>Input :</b> arr[] = {13, 6, 7, 12}
<b>Output :</b> _ 7 12 13 
<b>Explanation:</b>
Here, at index 0, 13 is the greatest value 
in given array and no other array element 
is greater from 13. So at index 0 we fill 
'-10000000'.
</pre>

<br>
<b>Example 2:</b>

<pre><b>Input :</b> arr[] = {6, 3, 9, 8, 10, 2, 1, 15, 7} <b>
Output :</b>  7 6 10 9 15 3 2 _ 8
<b>Explanation:</b> Here, at index 7, 15 is the greatest
value in given array and no other array element is
greater from 15. So at index 7 we fill '-10000000'.
</pre>

 

<b>Your Task:</b><br>
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function <b>greaterElement()</b> that takes an array <b>(arr)</b>, sizeOfArray <b>(n)</b>, and return an array that displays the next greater element to element at that index. The driver code takes care of the printing.

<b>Expected Time Complexity:</b> O(N*LOG(N)).<br>
<b>Expected Auxiliary Space:</b> O(N).

 

<b>Constraints:</b><br>
1 ≤ N ≤ 10<sup>5</sup><br>
-10<sup>6</sup> ≤ A<sub>i</sub> ≤ 10<sup>6</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Searching` `Sorting` `CPP` `STL` `Data Structures` `Algorithms`
- **Company Tags:** `Zoho`

### Related Articles
- [Smallest Greater Elements In Whole Array](https://www.geeksforgeeks.org/smallest-greater-elements-in-whole-array/)
