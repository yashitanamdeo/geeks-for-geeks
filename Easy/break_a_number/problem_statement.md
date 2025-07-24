<h1 align="center">Break a number</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.81%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 25K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a really large number N, break it into 3 whole numbers such that they sum up to the original number and find the number of ways to do so. Since this number can be very large, return it modulo 10<sup>9</sup>+7. 

 

<b>Example 1:</b>

<pre><b>Input:</b>
N = 2
<b>Output:</b>
6
<b>Explanation:</b>
Possible ways to break the number:
0 + 0 + 2 = 2 
0 + 2 + 0 = 2
2 + 0 + 0 = 2
0 + 1 + 1 = 2
1 + 1 + 0 = 2
1 + 0 + 1 = 2
</pre>

 

 

<b>Example 2:</b>

<pre><b>Input:</b>
N = 3
<b>Output:</b>
10
<b>Explanation:</b>
Possible ways to break the number:
0+0+3 = 3
0+3+0 = 3
3+0+0 = 3
0+1+2 = 3
0+2+1 = 3
1+0+2 = 3
1+2+0 = 3
2+0+1 = 3
2+1+0 = 3
1+1+1 = 3</pre>

 

 

<b>Your Task:</b>

You don't need to read input or print anything. Your task is to complete the function waysToBreakNumber() which takes an integer N and returns the possible ways to break the number in 3 parts.

 

<b>Expected Time Complexity:</b> O(1)<br>
<b>Expected Auxiliary Space:</b> O(1)

 

<b>Constraints:</b><br>
1 <= N <= 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `number-theory` `Mathematical` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Break Number Three Parts](https://www.geeksforgeeks.org/break-number-three-parts/)
