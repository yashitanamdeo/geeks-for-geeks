<h1 align="center">Paint N Houses</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.33%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 27K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There is a row of <b>N</b> houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color. Find the minimum cost to paint all houses.

The cost of painting each house in red, blue or green colour is given in the array <b>r[]</b>, <b>g[] </b>and <b>b[] </b>respectively.

<br><b>Example 1:</b>

<pre><b>Input</b>:
N = 3
r[] = {1, 1, 1}
g[] = {2, 2, 2}
b[] = {3, 3, 3}
<b>Output:</b> 4
<b>Explanation</b>: We can color the houses 
in RGR manner to incur minimum cost.
We could have obtained a cost of 3 if 
we coloured all houses red, but we 
cannot color adjacent houses with 
the same color.


</pre>

<br><b>Example 2:</b>

<pre><b>Input:</b>
N = 3
r[] = {2, 1, 3}
g[] = {3, 2, 1}
b[] = {1, 3, 2} 
<b>Output:</b> 3
<b>Explanation</b>: We can color the houses
in BRG manner to incur minimum cost.</pre>

<br><br><b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>distinctColoring</b><b>()</b> which takes the size <b>N </b>and the color arrays <b>r[]</b>, <b>g[]</b>, <b>b[] </b>as input parameters and returns the minimum cost of coloring such that the color of no two houses is same.<br><br> 

<b>Expected Time Complexity:</b> O(N)<br><b>Expected Auxiliary Space:</b> O(N)<br><br> 

<b>Constraints:</b><br>1 <= N <= 5*10<sup>4</sup><br>1 <= r[i], g[i], b[i] <= 10<sup>6</sup>


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `Walmart` `Google`

### Related Articles
- [Minimize Cost Of Painting N Houses Such That Adjacent Houses Have Different Colors](https://www.geeksforgeeks.org/minimize-cost-of-painting-n-houses-such-that-adjacent-houses-have-different-colors/)

### Related Interview Experiences
- [Walmart Lab Interview Experience Set 10 Campus](https://www.geeksforgeeks.org/walmart-lab-interview-experience-set-10-campus/)
