<h1 align="center">Fractional Knapsack</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 32.46%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 346K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two arrays, <b>val[]</b><b> </b>and <b>wt[]</b>, representing the values and weights of items, and an integer <b>capacity</b> representing the maximum weight a knapsack can hold, determine the maximum total value that can be achieved by putting items in the knapsack. You are allowed to break items into fractions if necessary.<br>Return the maximum value as a double, rounded to 6 decimal places.

<b>Examples :</b>

<pre><b>Input:</b> val[] = [60, 100, 120], wt[] = [10, 20, 30], capacity = 50
<b>Output: </b>240.000000<b>
Explanation: </b>Take the item with value 60 and weight 10, value 100 and weight 20 and split the third item with value 120 and weight 30, to fit it into weight 20. so it becomes (120/30)*20=80, so the total value becomes 60+100+80.0=240.0 Thus, total maximum value of item we can have is 240.00 from the given capacity of sack. 
</pre>

<pre><b>Input: </b>val[] = [60, 100], wt[] = [10, 20], capacity = 50
<b>Output: </b>160.000000<b>
Explanation: </b>Take both the items completely, without breaking. Total maximum value of item we can have is 160.00 from the given capacity of sack.</pre>

<pre><b>Input: </b>val[] = [10, 20, 30], wt[] = [5, 10, 15], capacity = 100
<b>Output: </b>60.000000<br><b>Explanation: </b>In this case, the knapsack capacity exceeds the combined weight of all items (5 + 10 + 15 = 30). Therefore, we can take all items completely, yielding a total maximum value of 10 + 20 + 30 = 60.000000.<br></pre>

<b>Constraints:</b><br>1 <= val.size=wt.size <= 10<sup>5</sup><br>1 <= capacity <= 10<sup>9</sup><br>1 <= val[i], wt[i] <= 10<sup>4</sup>

## Expected Complexities
- Time Complexity: O(n log n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Greedy` `Algorithms`
- **Company Tags:** `Microsoft`

### Related Articles
- [Fractional Knapsack Problem](https://www.geeksforgeeks.org/fractional-knapsack-problem/)
