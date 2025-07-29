<h1 align="center">Asteroid Collision</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.06%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 39K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

We are given an integer array <b>asteroids</b> of size <b>N</b> representing asteroids in a row. For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.<br>
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are of same size, both will explode. Two asteroids moving in the same direction will never meet.<br>
 

<b>Example 1:</b>

<b>Input:</b><br>
N = 3<br>
asteroids[ ] = {3, 5, -3}<br>
<b>Output: </b>{3, 5}<br>
<b>Explanation:</b> The asteroid 5 and -3 collide resulting in 5. The 5 and 3 never collide.
<b>Example 2:</b>

<b>Input:</b><br>
N = 2<br>
asteroids[ ] = {10, -10}<br>
<b>Output: </b>{ }<br>
<b>Explanation:</b> The asteroid -10 and 10 collide exploding each other.
<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>asteroidCollision()</b> which takes the array of integers <b>asteroids </b>and <b>N </b>as parameters and returns the state of asteroids after all collisions.

<b>Expected Time Complexity:</b> O(N)<br>
<b>Expected Auxiliary Space:</b> O(N)

<b>Constraints:</b><br>
1 ≤ N ≤ 10<sup>5</sup><br>
-1000 ≤ asteroids<sub>i  </sub>≤ 1000<br>
asteroids[i]!=0


<hr>

### Tags
- **Topic Tags:** `Arrays` `Stack` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Reduce Array By Replacing Adjacent Opposite Sign Pairs With Their Absolute Maximum](https://www.geeksforgeeks.org/reduce-array-by-replacing-adjacent-opposite-sign-pairs-with-their-absolute-maximum/)
