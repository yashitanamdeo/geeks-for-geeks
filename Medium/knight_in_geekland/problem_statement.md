<h1 align="center">Knight in Geekland</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 65.86%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 18K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Knight is at <b>(start_x,start_y)</b> in Geekland which is represented by an <b>NxM</b> 2D matrix.<br>Each cell in the matrix contains some points. In the ith step, the knight can collect all the points from all the cells that can be visited in exactly i steps without revisiting any cell.<br>Also, the knight has some magical powers that enable him to fetch coins from the future i.e. If the knight can collect y coins in the xth step he can fetch all the coins that he will collect in the (x + y)th step and if the knight can collect z coins in the (x + y)th step he can fetch all the coins that he will collect in the (x + y + z)th step and so on without increasing the step count i.e. knight will stay on xth step and will get all the coins of the future steps mentioned above((x + y)th step coins + (x + y+z)th steps + ...).

<b>For example</b>, If in 1st step knight can collect 1 point, then knight will also collect all the points which are at (1+1)th step i.e. 2 steps, and if knight can collect 3 points in (1+1)th step then knight will also collect all the points at (1+1+3)th step and so on. Hence being only at the first step knight can collect overall 1+3 = 4 points if there are no points available at (1+1+3)th step.

Find the minimum number of steps required to collect the maximum points.<br><b>Note:</b> The [knight moves](https://en.wikipedia.org/wiki/Knight_(chess)#:~:text=Compared%20to%20other%20chess%20pieces,pieces%20to%20reach%20its%20destination.) exactly the same as the knight on a chess board. Please follow 0 indexing.

Example 1:

<pre><b>Input:</b>
n = 9
m = 10
start_x = 4, start_y = 5
arr =
0 0 0 <b>2</b> 0 <b>2</b> 0 <b>2</b> 0 0
0 0 <b>2</b> 0 <b>2</b> 0 <b>2</b> 0 <b>2</b> 0
0 <b>2</b> 0 0 <b>1</b> <b>2</b> <b>0</b> 0 0 <b>2</b>
0 0 <b>2</b> <b>0</b> <b>2</b> 0 <b>2</b> <b>0</b> <b>2</b> 0
0 <b>2</b> 0 <b>2</b> 0 <b>0</b> 0 <b>2</b> 0 <b>2</b>
0 0 <b>2</b> <b>0</b> <b>2</b> 0 <b>2</b> <b>0</b> <b>2</b> 0
0 <b>2</b> 0 0 <b>0</b> <b>2</b> <b>0</b> 0 0 <b>2</b>
0 0 <b>2</b> 0 <b>2</b> 0 <b>2</b> 0 <b>2</b> 0
0 0 0 <b>2</b> 0 <b>2</b> 0 <b>2</b> 0 0
<b>Output:</b> 1
<b>Explanation:</b> minimum knight have to take 1 steps to gain maximum points.
Initially, the knight has 0 coins, he will take 1 step to collect 1 point (sum of cells denoted in red color).
Now in the second step, he can collect points from all the cells colored green i.e. 64 points.
But with his magical power, at the 1st step, he can fetch points from the (1 + 1)th step. Therefore he can collect 1 + 64 coins at step 1 only. Hence answer is 1.
</pre>

Example 2:

<pre>Input:
n = 3 
m = 3
start_x = 2, start_y = 1
arr =
7 6 8
9 1 4
6 2 8
Output:0
Explanation:
Initially, the knight has 2 points, or more formally we can say that at the 0th step knight has 2 points.
In the first step, he can collect points from cells (0, 0) and (0, 2) i.e. 15 points.
In the second step, he can collect points from cells (1, 0) and (1, 2) i.e. 13 coins.
In the third step, he can collect points from cells (2, 0) and (2, 2) i.e. 14 points.
In the fourth step, he can collect points from the cell (0, 1) i.e. 6 points.
So in each step, he can collect coins like -You can see in the below image  Knight can collect 15 coins in the 0th step only
<img src="https://media.geeksforgeeks.org/img-practice/rect46213-1668840290.png" alt="" title=""/>
</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function knightInGeekland() which takes 2-d array <b>arr[][],</b> starting coordinates of knight <b>start_x, and start_y </b>as input, and return an integer value as min steps to gain max points.

<b>Expected Time Complexity:</b> O(N*M)<br><b>Expected Auxiliary Space:</b> O(N*M)

<b>Constraints:</b><br>   1 <= len(arr), len(arr[0]) < 10<sup>3</sup><br>   0 <= values in arr <=100


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Matrix` `BFS`
- **Company Tags:** `None`

### Related Articles
- [Minimize Steps For Knight To Collect Maximum Points Knight In Geekland](https://www.geeksforgeeks.org/minimize-steps-for-knight-to-collect-maximum-points-knight-in-geekland/)
