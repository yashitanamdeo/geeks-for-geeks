<h1 align="center">Adventure in a Maze</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 38.8%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 12K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You have got a maze, which is a n*n Grid. Every cell of the maze contains these numbers 1, 2 or 3. <br>If it contains 1 : means we can go Right from that cell only.<br>If it contains 2 : means we can go Down from that cell only.<br>If it contains 3 : means we can go Right and Down to both paths from that cell.<br>We cant go out of the maze at any time.<br>Initially, You are on the Top Left Corner of The maze(Entry). And, You need to go to the Bottom Right Corner of the Maze(Exit).<br>You need to find the total number of paths from Entry to Exit Point.<br>There may be many paths but you need to select that path which contains the maximum number of Adventure.<br>The Adventure on a path is calculated by taking the sum of all the cell values thatlies in the path.<br> 

<b>Example 1:</b>

<pre><b>Input: </b>matrix = {{1,1,3,2,1},{3,2,2,1,2},
{1,3,3,1,3},{1,2,3,1,2},{1,1,1,3,1}}
<b>Output: </b>{4,18}
<b>Explanation: </b>There are total 4 Paths Available 
out of which The Max Adventure is 18. Total 
possible Adventures are 18,17,17,16. Of these 
18 is the maximum.
</pre>

 

<b>Your Task:</b><br>You don't need to read or print anything. Your task is to complete the function <b>FindWays() </b>which takes matrix as input parameter and returns a list containg total number of ways to reach at (n, n) modulo 10<sup>9</sup> + 7 and maximum number of Adventure.<br> 

<b>Expected Time Complexity: </b>O(n<sup>2</sup>)<br><b>Expected Space Complexity: </b>O(n<sup>2</sup>)<br> 

<b>Constraints:</b><br>1 <= n <= 100


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Matrix` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Count Number Of Paths With Maximum Sum Path From Top Left To Bottom Right Cell Of A Maze Adventure In A Maze](https://www.geeksforgeeks.org/count-number-of-paths-with-maximum-sum-path-from-top-left-to-bottom-right-cell-of-a-maze-adventure-in-a-maze/)
