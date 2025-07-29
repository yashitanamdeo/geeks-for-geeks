<h1 align="center">Convert an array to reduced form</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 54.74%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 47K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array with <b>N</b> distinct elements, convert the given array to a reduced form where all elements are in range from <b>0</b> to <b>N-1</b>. The order of elements is same, i.e., <b>0</b> is placed in place of smallest element, <b>1</b> is placed for second smallest element, and <b>N-1</b> is placed for the largest element.

<b>Note: </b>You don't have to return anything. You just have to change the given array.

<b>Example 1:</b>

<pre><b>Input:
</b>N = 3
Arr[] = {10, 40, 20}
<b>Output: </b>0 2 1
<b>Explanation:</b> 10 is the least element so it
is replaced by 0. 40 is the largest
element so it is replaced by 3-1 = 2. And
20 is the 2nd smallest element so it is
replaced by 1.
</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>N = 5
Arr[] = {5, 10, 40, 30, 20}
<b>Output:</b> 0 1 4 3 2
<b>Explanation:</b> As 5 is smallest element,
it's replaced by 0. Then 10 is 2nd
smallest element, so it's replaced by 1.
Then 20 is 3rd smallest element, so it's
replaced by 2. And so on.
</pre>

<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>convert()</b> which takes the array of integers <b>arr </b>and <b>n </b>as parameters and makes changes in the given array.

<b>Expected Time Complexity:</b> O(N*logN)<br>
<b>Expected Auxiliary Space:</b> O(N)

<b>Constraints:</b><br>
1 ≤ N ≤ 10<sup>5</sup><br>
1 ≤ Arr[i] ≤ 10<sup>6</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Sorting` `Data Structures` `Algorithms`
- **Company Tags:** `None`
