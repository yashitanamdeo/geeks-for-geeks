<h1 align="center">Unique Number of Occurrences</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 57.68%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 51K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr</b> of <b>N</b> integers, the task is to check whether the frequency of the elements in the array is unique or not. Or in other words, there are no two <b>distinct</b> numbers in array with equal frequency. If all the frequency is unique then return <b>true</b>, else return <b>false</b>.

<b>Example 1:</b>

<pre><b>I</b><b>nput:</b>
N = 5<br>arr = [1, 1, 2, 5, 5]
<b>Output:</b>
false
<b>Explanation:<br></b>The array contains 2 (1’s), 1 (2’s) and 2 (5’s), since the number of frequency of 1 and 5 are the same i.e. 2 times. Therefore, this array does not satisfy the condition.
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N = 10<br>arr = [2, 2, 5, 10, 1, 2, 10, 5, 10, 2]
<b>Output:</b>
true
<b>Explanation:</b>
Number of 1’s -> 1
Number of 2’s -> 4
Number of 5’s -> 2
Number of 10’s -> 3.
Since, the number of occurrences of elements present in the array is unique. Therefore, this array satisfy the condition.</pre>

<b>Your task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>isFrequencyUnique()</b> which take integer <b>N</b> and array <b>arr</b> of size N as arguments, and returns a boolean.

<b>Expected Time Complexity:</b> O(N)<br><b>Expected Auxiliary Space:</b> O(N)

<b>Constraints:</b><br>1 <= N <=10<sup>5</sup><br>-10<sup>9</sup> <= arr[i] <= 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `set` `Sorting` `Map`
- **Company Tags:** `PayPal` `Bloomberg` `Adobe` `Google` `Amazon` `Apple`

### Related Articles
- [Check If Frequency Of Each Element In Given Array Is Unique Or Not](https://www.geeksforgeeks.org/check-if-frequency-of-each-element-in-given-array-is-unique-or-not/)
