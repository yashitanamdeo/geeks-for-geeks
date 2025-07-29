<h1 align="center">Maximum Number of coins</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 67.12%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 19K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

We have been given N balloons, each with a number of coins associated with it. On bursting a balloon i, the number of coins gained is equal to A[i-1]*A[i]*A[i+1].<br>
Also, balloons i-1 and i+1 now become adjacent. Find the maximum possible profit earned after bursting all the balloons. Assume an extra 1 at each boundary.

<b>Example 1:</b>

<pre><b>Input</b><b>:</b> 
N=2
a[]={5, 10}
<b>Output:</b> 
60
<b>Explanation:</b> First Burst 5, Coins = 1*5*10
              Then burst 10, Coins+= 1*10*1
              Total = 60</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N=4
a[] = {3,1,5,8}
<b>Output:
</b>167
<b>Explanation:</b>
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167.</pre>

<b>Your Task:  </b><br>
You don't need to read input or print anything. Your task is to complete the function <b>maxCoins()</b> which takes the array arr[], its size N, and returns the maximum number of coins that can be collected.

<b>Expected Time Complexity:</b> O(N^3)<br>
<b>Expected Space Complexity:</b> O(N^2)

<b>Constraints:</b><br>
1 <= N <= 400<br>
0 <= a[i] <= 100<br>


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Matrix` `Data Structures` `Algorithms`
- **Company Tags:** `MakeMyTrip`
