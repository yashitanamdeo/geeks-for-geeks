<h1 align="center">Max Coins</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 52.73%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 24K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a 2D integer array <b>ranges </b>whose length is <b>n </b>where <b>ranges[i]=[start<sub>i</sub>, end,coins<sub>i</sub>]</b> means all integers from start<sub>i</sub> to end<sub>i</sub> inclusive start<sub>i</sub> and end<sub>i</sub> are present and we get <b>coins<sub>i</sub></b> amount of <b>coins</b> when we select this <b>i<sup>th</sup></b> range. You can select <b>at most</b> two intervals so as to collect maximum coins but if you select two ranges then those two ranges <b>should not intersect or overlap but can touch each other.</b>

<b>Note</b>: <br>1. You can select at max 2 ranges and they should not intersect with each other but they can touch themselves.<br>2. Two ranges (A1,A2) and (A3,A4) are overlapping when A3<A2, for example (2,3) and (2,4) are overlapping, (2,5) and (4,6) are overlapping, but (2,3) and (3,4) are not overlapping also (2,2) and (2,2) are not overlapping.

<b>Example 1:</b>

<pre><b>Input :
</b>n=3
ranges={{1,3,4},{2,3,5},{3,4,2}}
<b>Output: </b>7
<b>Explanation:</b>
We can see that we can take 2nd and 
3rd ranges as they are not intersecting
(only touching) we get maximum Coins by 
taking these ranges(5+2=7).</pre>

<b>Example 2:</b>

<pre><b>Input :</b>
n=5
ranges={{1,3,4},{2,3,5},{3,4,2},{5,8,9},{2,8,10}}
<b>Output: </b>14
<b>Explanation:</b>
We can see that we can take 2nd and 
4th ranges as they are not intersecting 
we get maximum Coins(5+9=14) by taking 
these ranges.</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>maxCoins()</b> which takes an integer <b>n</b>(<b>length of ranges</b>), integer 2D integer array<b> ranges, </b>and you have to return the <b>maximum</b> number of <b>coins</b> you got after selecting <b>at most</b> two ranges that are not intersecting.

<b>Expected Time Complexity:</b> O(nlogn)<br><b>Expected Space Complexity:</b> O(n)<br><br><b>Constraints:</b><br>1<=<b>n</b><=10<sup>5</sup><br>0<=<b>ranges</b>[i][0]<=<b>ranges</b>[i][1]<=10<sup>9</sup><br>0<=<b>ranges</b>[i][2](coins)<=10<sup>6</sup><br>The sum of n over all test cases won't exceed 10<sup>6</sup>


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Greedy` `Sorting` `Algorithms`
- **Company Tags:** `None`
