<h1 align="center">Apple Sequences</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 54.04%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 24K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There is a string of size <b>n</b> containing only '<b>A'</b> and '<b>O'</b>. '<b>A'</b> stands for Apple, and '<b>O'</b> stands for Orange. We have <b><i>m</i></b> number of spells, each spell allows us to convert an orange into an apple. 

Find the longest subarray of apples you can make, given a string and the value of <b>m</b>.

<br><b>Example 1:</b>

<pre><b>Input</b>:
N = 5
M = 1
arr[] = 'AAOAO'
<b>Output:</b> 4 
<b>Explanation</b>: Changing the orange at 
3rd position into an apple gives 
us the maximum possible answer.
</pre>

<br><b>Example 2:</b>

<pre><b>Input:</b>
N = 5
M = 1
arr = 'AOOAO'
<b>Output: </b>2
<b>Explanation</b>: Changing any orange into 
an apple will give us a sequence 
of length 2.</pre>

<br><b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>appleSequence</b><b>()</b> which takes the array in the form of a string, its size n,<b> </b>and an integer m<b> </b>as input parameters and returns the largest apple sequences after converting m oranges.

<b>Expected Time Complexity:</b> O(n)<br><b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>1 <= m <= n <= 10<sup>6</sup>


<hr>

### Tags
- **Topic Tags:** `two-pointer-algorithm` `implementation` `Algorithms`
- **Company Tags:** `Ola Cabs`

### Related Articles
- [Find The Longest Sequence Of Apples](https://www.geeksforgeeks.org/find-the-longest-sequence-of-apples/)

### Related Interview Experiences
- [Ola Interview Experience](https://www.geeksforgeeks.org/ola-interview-experience/)
