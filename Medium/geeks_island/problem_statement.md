<h1 align="center">Geeks Island</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 60.27%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 17K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Geeks Island is represented by an <b>N * M</b> matrix <b>mat</b>. The island is touched by the Indian Ocean from the top and left edges and the Arabian Sea from the right and bottom edges. Each element of the matrix represents the height of the cell.

Due to the rainy season, the island receives a lot of rainfall, and the water can flow in four directions(up, down, left, or right) from one cell to another one with <b>height equal or lower</b>.

You need to find the number of cells from where water can flow to both the Indian Ocean and the Arabian Sea.

<b>Example 1:</b>

<pre><b>Input:</b>
N = 5, M = 5
mat[][] =    {{1, 3, 3, 2, 4},
               {4, 5, 6, 4, 4},
               {2, 4, 5, 3, 1},
               {6, 7, 1, 4, 5},
               {6, 1, 1, 3, 4}}
<b>Output:</b>
8
<b>Explanation:</b>
Indian    ~   ~   ~   ~   ~
Ocean  ~  1   3   3   2  (4) *
        ~  4   5  (6) (4) (4) *
        ~  2   4  (5)  3   1  *
        ~ (6) (7)  1   4   5  *
        ~ (6)  1   1   3   4  *           
           *   *   *   *   * Arabian Sea
Water can flow to both ocean and sea from the cells
denoted by parantheses().For example at index(1,2), the height of that island is 6. If a water drop falls on that island, water can flow to up direction(as 3<=6) and reach to Indian Ocean. ALso, water can flow to right direction(as 6>=4>=4) and reach to Arabian Sea.</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N = 2, M = 3
mat[][] =    {{1, 1, 1},
               {1, 1, 1}}
<b>Output:</b>
6 
<b>Explanation:</b>
Water can flow from all cells to both Indian Ocean and Arabian Sea as the height of all islands are same.</pre>

<b>Your Task:</b>

Your task is to complete the function <b>water_flow() </b>which takes an integer array <b>mat</b>, integer <b>N</b> and integer <b>M</b> as the input parameter and returns an integer, denoting the number of cells from which water can to both ocean and sea.

<b>Expected Time Complexity</b> : O(N*M)<br>
<b>Expected Auxiliary Space</b> : O(N*M)

<b>Constraints:</b>

- 1 <= N, M <= 10<sup>3</sup>
- 1 <= mat[i][j] <= 10<sup>6</sup>


<hr>

### Tags
- **Topic Tags:** `DFS` `Matrix`
- **Company Tags:** `None`
