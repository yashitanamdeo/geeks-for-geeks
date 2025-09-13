<h1 align="center">Minimum Cost to cut a board into squares</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 60.83%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 25K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a board of dimensions <b>n × m</b> that needs to be cut into <b>n*m</b> squares. The cost of making a cut along a horizontal or vertical edge is provided in two arrays:

- <b>x[]:</b> Cutting costs along the vertical edges (length-wise).
- <b>y[]: </b>Cutting costs along the horizontal edges (width-wise).
Find the <b>minimum total cost</b> required to cut the board into squares optimally.

<b>Examples:<br></b>

<pre><b>Input:</b> n = 4, m = 6, x[] = [2, 1, 3, 1, 4], y[] = [4, 1, 2]
<b>Output: </b>42
<b>Explanation:</b>
<img style="height: 218px; width: 327px;" src="https://media.geeksforgeeks.org/img-practice/board-1646284249.png" alt="" title=""/>
Initially no. of horizontal segments = 1 & no. of vertical segments = 1.<br>Optimal way to cut into square is:<br>• Pick 4 (from x) -> vertical cut, Cost = 4 × horizontal segments = 4,<br>  Now, horizontal segments = 1, vertical segments = 2.<br>• Pick 4 (from y) -> horizontal cut, Cost = 4 × vertical segments = 8,<br>  Now, horizontal segments = 2, vertical segments = 2.<br>• Pick 3 (from x) -> vertical cut, Cost = 3 × horizontal segments = 6,<br>  Now, horizontal segments = 2, vertical segments = 3.<br>• Pick 2 (from x) -> vertical cut, Cost = 2 × horizontal segments = 4,<br>  Now, horizontal segments = 2, vertical segments = 4.<br>• Pick 2 (from y) -> horizontal cut, Cost = 2 × vertical segments = 8,<br>  Now, horizontal segments = 3, vertical segments = 4.<br>• Pick 1 (from x) -> vertical cut, Cost = 1 × horizontal segments = 3,<br>  Now, horizontal segments = 3, vertical segments = 5.<br>• Pick 1 (from x) -> vertical cut, Cost = 1 × horizontal segments = 3,<br>  Now, horizontal segments = 3, vertical segments = 6.<br>• Pick 1 (from y) -> horizontal cut, Cost = 1 × vertical segments = 6,<br>  Now, horizontal segments = 4, vertical segments = 6.<br>So, the total cost = 4 + 8 + 6 + 4 + 8 + 3 + 3 + 6 = 42.</pre>

<pre><b>Input:</b> n = 4, m = 4, x[] = [1, 1, 1], y[] = [1, 1, 1]<br><b>Output: </b>15<b>
Explanation:</b> 
<img style="height: 225px; width: 323px;" src="https://media.geeksforgeeks.org/img-practice/board-1646284249-1661926688.png" alt="" title=""/>
Initially no. of horizontal segments = 1 & no. of vertical segments = 1.
Optimal way to cut into square is: <br>• Pick 1 (from y) -> horizontal cut, Cost = 1 × vertical segments = 1,
  Now, horizontal segments = 2, vertical segments = 1.
• Pick 1 (from y) -> horizontal cut, Cost = 1 × vertical segments = 1,
  Now, horizontal segments = 3, vertical segments = 1.
• Pick 1 (from y) -> horizontal cut, Cost = 1 × vertical segments = 1,
  Now, horizontal segments = 4, vertical segments = 1.
• Pick 1 (from x) -> vertical cut, Cost = 1 × horizontal segments = 4,
  Now, horizontal segments = 4, vertical segments = 2.
• Pick 1 (from x) -> vertical cut, Cost = 1 × horizontal segments = 4,
  Now, horizontal segments = 4, vertical segments = 3.
• Pick 1 (from x) -> vertical cut, Cost = 1 × horizontal segments = 4,
  Now, horizontal segments = 4, vertical segments = 4<br>So, the total cost = 1 + 1 + 1 + 4 + 4 + 4 = 15.</pre>

<b>Constraints:</b><br>2 ≤ n, m ≤ 10<sup>3<br></sup>1 ≤ x[i], y[j] ≤10<sup>3</sup>

## Expected Complexities
- Time Complexity: O(n*logn + m*logm)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Greedy` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Minimum Cost Cut Board Squares](https://www.geeksforgeeks.org/minimum-cost-cut-board-squares/)
