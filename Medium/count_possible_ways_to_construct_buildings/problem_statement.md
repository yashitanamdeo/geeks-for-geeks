<h1 align="center">Count possible ways to construct buildings</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 38.53%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 60K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There is a road passing through a city with <b>N</b> plots on both sides of the road. Plots are arranged in a straight line on either side of the road. Determine the <b>total number </b>of ways to construct buildings in these plots, ensuring that no two buildings are adjacent to each other. Specifically, buildings on opposite sides of the road cannot be adjacent.

Using <b>*</b> to represent a plot and <b>||</b> for the road, the arrangement for <b>N = 3 </b>can be visualized as follows: <b>* * * || * * </b>*.

<b>Note:</b> As the answer can be very large, print it <b>mod 10<sup>9</sup>+7</b>.

<b>Example 1:</b>

<pre><b>Input: </b>N = 1
<b>Output: </b>4
<b>Explanation: <br></b>Possible ways for the arrangement are B||*, *||B, B||B, *||*<br>where B represents a building.</pre>

<b>Example 2:</b>

<pre><b>Input: </b>N = 3
<b>Output: </b>25
<b>Explanation: <br></b>Possible ways for one side are BSS, BSB, SSS, SBS,<br>SSB where B represents a building and S
represents an empty space. Pairing up with <br>possibilities on the other side of the road,<br>total possible ways are 25.
</pre>

<b>Your Task:</b><br>You don't need to read or print anything. Your task is to complete the function <b>TotalWays()</b> which takes <b>N</b> as input parameter and returns the total possible ways modulo <b>10<sup>9</sup> + 7</b>.<br> 

<b>Expected Time Complexity: </b>O(N)<br><b>Expected Space Complexity: </b>O(N)<br> 

<b>Constraints:</b><br>1 <= N <= 100000


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Fibonacci` `Algorithms`
- **Company Tags:** `Payu`

### Related Articles
- [Count Possible Ways To Construct Buildings](https://www.geeksforgeeks.org/count-possible-ways-to-construct-buildings/)

### Related Interview Experiences
- [Payu Interview Experience Set 6 On Campus](https://www.geeksforgeeks.org/payu-interview-experience-set-6-on-campus/)
