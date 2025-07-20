<h1 align="center">Minimize Max Distance to Gas Station</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 38.36%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 90K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 40m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

We have a horizontal number line. On that number line, we have gas <b>stations </b>at positions stations[0], stations[1], ..., stations[n-1], where <b>n </b>is the size of the stations array. Now, we add <b>k</b> more gas stations so that <b>d</b>, the maximum distance between adjacent gas stations, is minimized. We have to find the smallest possible value of d. Find the answer <b>exactly</b> to 2 decimal places.<br><b>Note</b>: <b>stations</b> is in a <b>strictly increasing</b> order.

<b>Example 1:</b>

<pre><b>Input:
</b>n = 10
stations[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 9
<b>Output:</b> 0.50
<b>Explanation: </b>Each of the 9 stations can be added mid way between all the existing adjacent stations.</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>n = 10
stations[] = [3, 6, 12, 19, 33, 44, 67, 72, 89, 95] <br>k = 2 <br><b>Output:</b> 14.00 <br><b>Explanation: </b>Construction of gas stations at 8th(between 72 and 89) and 6th(between 44 and 67) locations.</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>findSmallestMaxDist() </b>which takes a list of stations and integer k as inputs and returns the smallest possible value of d. Find the answer <b>exactly</b> to 2 decimal places.

<b>Constraint:</b><br>10 <= n <= 10000<sup> </sup><br>0 <= stations[i] <= 10<sup>9 </sup><br>0 <= k <= 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n log k)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Binary Search` `Mathematical` `Arrays` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Minimize The Maximum Distance Between Adjacent Points After Adding K Points Anywhere In Between](https://www.geeksforgeeks.org/minimize-the-maximum-distance-between-adjacent-points-after-adding-k-points-anywhere-in-between/)
