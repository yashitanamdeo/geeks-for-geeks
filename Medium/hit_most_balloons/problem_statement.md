<h1 align="center">Hit most Balloons</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 39.54%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 8K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an infinite two-dimensional grid. There are <b>N </b>balloons placed at certain coordinates of the grid. You have an arrow with yourself, which you will be using to shoot the balloons. You can select any point on the grid as your starting point and any point on the grid as the target point. When you fire the arrow, all ballons lying on the shortest path between the starting point and target point will be burst. Given the coordinates of the N ballons in an array <b>arr, </b>your task is to find out the maximum number of balloons that you can fire in one arrow shot.

<b>Example 1:</b>

<pre><b>Input:</b>
N = 3
arr[] = {{1, 2}, {2, 3}, {3, 4}}
<b>Output:</b>
3
<b>Explanation:</b>
If you position yourself at point (1,2)
and fire the arrow aiming at the point (3,4).
Then all the balloons will burst.</pre>

<b>Example 2:</b>

<pre><b>Input: </b>
N = 3
arr[] = {{2,2}, {0,0}, {1,2}} 
<b>Output:</b>
2
<b>Explanation: </b>
If you position yourself at point (2,2)
and fire the arrow aiming at the point (0,0).
Then the two balloons present at the two points
will burst.
</pre>

<b>Your Task:</b><br>
Complete the function <b>mostBalloons</b><b>()</b> which takes the integers <b>N </b>and the array <b>arr </b>as the input parameters, and returns the maximum number of balloons that can be burst using one arrow.

<b>Expected Time Complexity:</b> O(N<sup>2</sup>)<br>
<b>Expected Auxiliary Space:</b> O(N)

<b>Constraints:</b><br>
1 ≤ N ≤ 10<sup>3</sup><br>
-10<sup>9</sup> ≤ arr[i][j] ≤ 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Mathematical` `Geometric` `Algorithms`
- **Company Tags:** `PayPal`

### Related Articles
- [Count Maximum Points On Same Line](https://www.geeksforgeeks.org/count-maximum-points-on-same-line/)

### Related Interview Experiences
- [Paypal Interview Experience Sde 1 On Campus](https://www.geeksforgeeks.org/paypal-interview-experience-sde-1-on-campus/)
