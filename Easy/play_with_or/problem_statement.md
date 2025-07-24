<h1 align="center">Play With OR</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 75.8%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 64K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array <b>arr[] </b>of length <b>n</b>, you have to <b>re-construct the same</b> array <b>arr[] in-place</b>. The <b>arr[i]</b> after reconstruction will become <b>arr[i] OR arr[i+1], </b>where <b>OR </b>is [<b>bitwise or</b>](https://www.geeksforgeeks.org/bitwise-operators-in-c-cpp/). If for some <b>i</b>, <b>i+1</b> does not exists, then do not change <b>arr[i]</b>.

<b>Example 1:</b>

<pre><b>Input :<br></b>n = 5<br>arr[] = {10, 11, 1, 2, 3}
<b>Output :</b><br>11 11 3 3 3
<b>Explanation:</b>
At index 0, arr[0] or arr[1] = 11
At index 1, arr[1] or arr[2] = 11
At index 2, arr[2] or arr[3] = 3
...
At index 4, No element is left So, it will remain as it is.
New Array will be {11, 11, 3, 3, 3}.</pre>

<b>Example 2:</b>

<pre><b>Input :<br></b>n= 4<br>arr[] = {5, 9, 2, 6} <b>
Output :</b><br>13 11 6 6<br><b>Explanation:<br></b>At index 0, arr[0] or arr[1] = 13.<br>At index 1, arr[1] or arr[2] = 11.<br>At index 2, arr[2] or arr[3] = 6.<br>At index 3, No element is left So, it will remain as it is.<br>New Array will be {13, 11, 6, 6}.</pre>

<b>Your Task:</b><br>You are required to implement the function <b>game_with_number()</b>, which takes an array <b>arr</b>, representing values at each index, and the size of the array <b>n</b>. The function should modify the elements of the <b>same array arr[] in-place </b>by replacing them with the values obtained by performing the <b>bitwise OR</b> operation on consecutive elements.<br>

<b>Expected Time Complexity:</b> O(n).<br><b>Expected Auxiliary Space:</b> O(1).

<b>Constraints:<br></b>1 ≤ n ≤ 10<sup>5</sup><br>1 ≤ arr[i] ≤ 10<sup>7</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Bit Magic` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Reconstruct The Array By Replacing Arri With Arri 11 M](https://www.geeksforgeeks.org/reconstruct-the-array-by-replacing-arri-with-arri-11-m/)
