<h1 align="center">Wine Buying and Selling</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 62.43%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 17K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 10m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array, Arr[] of size N represents N house built along a straight line with equal distance between adjacent houses. Each house has a certain number of wine and they want to buy/sell those wines to other houses. Transporting one bottle of wine from one house to an adjacent house results in one unit of work. The task is to find the minimum number of work is required to fulfill all the demands of those N houses.

1. if arr[i] < 0, then ith house wants to sell arr[i] number of a wine bottle to other houses.
1. if arr[i] > 0, then ith house wants to buy arr[i] number of a wine bottle from other houses.
<b>Note:</b> One have to print the minimum number such that, all the house can buy/sell wine to each other.<br>
It is guaranteed that sum of all the elements of the array will be 0.

<b>Example 1:</b>

<pre><b>Input:</b> N = 5,
Arr[] = {5, -4, 1, -3, 1}
<b>Output:</b> 9
<b>Explanation: </b>
1th house can sell 4 wine bottles to 0th house,
total work needed 4*(1-0) = 4, new arr[] = 1,0,1,-3,1
now 3rd house can sell wine to 0th, 2th and 4th.
so total work needed = 1*(3-0)+1*(3-2)+1*(4-3) = 5
So total work will be 4+5 = 9</pre>

<b>Example 2: </b>

<pre><b>Input:</b> N = 6,
Arr[]={-1000, -1000, -1000, 1000, 1000, 1000}
<b>Output:</b> 9000
<b>Explanation: </b> 
0th house sell 1000 wine bottles to 3rd house, 
total work needed 1000*(3-0) = 3000. 
1st house sell 1000 wine bottles to 4th house,
total work needed 3000 + 1000*(3-0) = 6000.
2nd house sell 1000 wine bottles to 5th house,
total work needed 6000 + 1000*(3-0) = 9000. 
So total work will be 9000 unit.
</pre>

<b>Your Task:  </b><br>
You don't need to read input or print anything. Complete the function <b>wineSelling()</b> which takes the array Arr[] and its size N as input parameters and returns an integer as output.

<b>Expected Time Complexity: </b>O(N)<br>
<b>Expected Auxiliary Space:</b> O(N)

<br>
<b>Constraints:</b><br>
1 ≤ N ≤ 10^5<br>
-10^6 ≤ Arr[i] ≤ 10^6


<hr>

### Tags
- **Topic Tags:** `Arrays` `Greedy` `Data Structures` `Algorithms`
- **Company Tags:** `None`
