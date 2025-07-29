<h1 align="center">Make the array beautiful</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 49.96%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 62K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of negative and non-negative integers. You have to make the array beautiful. An array is beautiful if two adjacent integers, arr[i] and arr[i+1] are either negative or non-negative. And you can do the following operation any number of times until the array becomes beautiful.

- If two adjacent integers are different i.e. one of them is negative and other is non-negative, remove them.
Return the beautiful array after performing the above operation.

<b>Note:</b>An empty array is also a beautiful array. There can be many adjacent integers which are different as stated above. So remove different adjacent integers as described above from <b>left to right</b>.

<b>Example 1:</b>

<pre><b>Input: </b>4 2 -2 1<b>
Output: </b>4 1
<b>Explanation:</b> As at indices 1 and 2 , 2 and -2 have
different sign, they are removed. And the  the final
array is: 4 1.
</pre>

<b>Example 2:</b>

<pre><b>Input: </b>2 -2 1 -1<b>
Output: </b>[]<b>
Explanation: </b>As at indices 0 and 1, 2 and -2 have
different sign, so they are removed. Now the array
is 1 -1.Now 1 and -1 are also removed as they have
different sign. So the final array is empty. </pre>

<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>makeBeautiful() </b>which takes an array as an input parameter and returns an array.

<b>Expected Time Complexity:</b> O(N)<br>
<b>Expected Space Complexity:</b> O(N)

<br>
<b>Constraints:</b><br>
1 <= size of the array <= 10<sup>5</sup><br>
-10<sup>5</sup> <= arr[i] <= 10<sup>5</sup><br>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Stack` `Data Structures`
- **Company Tags:** `None`
