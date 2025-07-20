<h1 align="center">Remove the balls</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 58.66%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 45K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given two arrays, <b>color</b> and <b>radius</b>, representing a sequence of balls:

 

- <b>color[i]</b> is the color of the i-th ball.
- <b>radius[i]</b> is the radius of the i-th ball.
 

If two <b>consecutive</b> balls have the <b>same color </b>and <b>radius</b>, remove them both. Repeat this process until no more such pairs exist.

 

Return the <b>number </b>of<b> </b>balls <b>remaining</b> after all possible removals.

<b>Examples:</b>

<pre><b>Input</b>: color[] = [2, 3, 5], radius[] = [3, 3, 5]
<b>Output: </b>3
<b>Explanation</b>: All the 3 balls have different colors and radius.</pre>

<pre><b>Input: </b>color[] = [2, 2, 5], radius[] = [3, 3, 5]<b><br>Output:</b> 1
<b>Explanation</b>: First ball and second ball have same color 2 and same radius 3. So, after removing only one ball is left. It cannot be removed from the array. Hence, the final array has length 1.</pre>

<b>Constraints:</b><br>1 ≤ color.size() = radius.size() ≤ 10<sup>5</sup><br>1 ≤ color[i] ≤ 10<sup>9</sup><sup> <br></sup>1 ≤ radius[i] ≤ 10<sup>9</sup><sup>  </sup><sup>                                                                                                                                         </sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Stack` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Length Of Array After Removing Consecutive Balls](https://www.geeksforgeeks.org/length-of-array-after-removing-consecutive-balls/)
