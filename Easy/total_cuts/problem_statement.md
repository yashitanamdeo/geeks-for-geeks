<h1 align="center">Total Cuts</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 54.24%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 28K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array <b>A</b> of <b>N</b> integers and an integer <b>K</b>, and your task is to find the total number of cuts that you can make such that for each cut these two conditions are satisfied<br>
1. A cut divides an array into two parts equal or unequal length (non-zero).<br>
2. Sum of the largest element in the left part and the smallest element in the right part is greater than or equal to K.

<b>Example 1:</b>

<pre><b>Input:</b>
N=3
K=3
A[]={1,2,3}
<b>Output:</b>
2
<b>Explanation:</b>
Two ways in which array is divided to satisfy above conditions are:
{1} and {2,3} -> 1+2>=3(satisfies the condition)
{1,2} and {3} -> 2+3>=3(satisfies the condition)</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N=5
K=5
A[]={1,2,3,4,5}
<b>Output:</b>
3
<b>Explanation:</b>
{1,2} and {3,4,5} -> 2+3>=5
{1,2,3} and {4,5} -> 3+4>=5
{1,2,3,4} and {5} -> 4+5>=5</pre>

<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function totalCuts() which takes two integers N, K, and an array A of size N as input parameters, and returns an integer representing the total number of cuts that satisfy both conditions.

<b>Expected Time Complexity:</b> O(N)<br>
<b>Expected Auxiliary Space:</b> O(N)

<b>Constraints:</b><br>
1 <= N <= 10^6<br>
0 <= K <= 10^6<br>
0 <= A[i] <= 10^6


<hr>

### Tags
- **Topic Tags:** `prefix-sum` `Arrays` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Total Cuts Such That Sum Of Largest Of Left And Smallest Of Right Is Atleast K](https://www.geeksforgeeks.org/total-cuts-such-that-sum-of-largest-of-left-and-smallest-of-right-is-atleast-k/)
