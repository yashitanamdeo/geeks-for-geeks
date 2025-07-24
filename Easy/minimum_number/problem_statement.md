<h1 align="center">Minimum Number</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.41%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 27K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array <b>arr </b>of <b>n </b>elements. In one operation you can pick two indices <b>i </b>and <b>j</b>, such that <b>arr[i] >= arr[j]</b> and replace the value of <b>arr[i]</b> with <b>(arr[i] - arr[j])</b>. You have to <b>minimize</b> the values of the array after performing any number of such operations.

<b>Example 1:</b>

<pre><b>Input:</b>
n = 3
arr = {3,2,4}
<b>Output:</b>
1
<b>Explanation:</b>
1st Operation : We can pick 4 & 3, subtract 4-3 => {3,2,1}
2nd Opeartion : We can pick 3 & 2, subtarct 3-2 => {1,2,1}
3rd Operation : We can pick 1 & 2, subtract 2-1 => {1,1,1}
4th Opeartion : We can pick 1 & 1, subtract 1-1 => {1,0,1}
5th Operation : We can pick 1 & 1, subtract 1-1 => {0,0,1}
After this no operation can be performned, so maximum no is left in the array is 1, so the ans is 1.
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
n = 2
arr = {2,4}
<b>Output:</b>
2
<b>Explanation:</b>
1st Operation : We can pick 4 & 2, subtract 4-2 => {2,2}
2nd Operation : We can pick 2 & 2, subtract 2-2 => {0,2}
After this no operation can be performned, so maximum no is left in the array is 2, so the ans is 2.
</pre>

<b>Your Task:  </b><br>
You don't need to read input or print anything. Your task is to complete the function <b>minimumNumber() </b>which takes an integer <b>n </b>and an array <b>arr</b>, as input parameters and returns the <b>maximum</b> number which is minimized after performing operations.

<b>Expected Time Complexity</b>: O(n)<br>
<b>Expected Space Complexity</b>: O(1)

<b>Constraints:</b><br>
1 ≤ n ≤ 10<sup>5</sup><br>
1 ≤ arr[i] ≤ 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures` `Algorithms`
- **Company Tags:** `None`
