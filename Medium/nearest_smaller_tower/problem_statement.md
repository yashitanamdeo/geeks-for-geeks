<h1 align="center">Nearest smaller tower</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 55.45%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 28K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array where each element <b>arr[i]</b> represents the height of the tower. Find for each tower, the nearest possible tower that is shorter than it. You can look left or right on both sides.<br><b>Note : </b>

- 
If two smaller towers are at the same distance, pick the smallest tower.


- 
If two towers have the same height then we choose the one with a smaller index.


<b>Examples:</b>

<pre><b>Input: </b>arr[] = [1, 3, 2]
<b>Output: </b>[-1, 0, 0] 
<b>Explanation:</b>
For <b>0th</b> index : no tower is smallest, so <b>-1</b>.
For <b>1st</b> index : For 3, here 1 & 2 both are 
small & at a same distance, so we will pick 1, 
beacuse it has smallest value, so <b>0(index)</b>
For <b>2nd</b> Index : here 1 is smaller, so <b>0(index)
</b>So the final output will be which consistes 
indexes are [-1, 0, 0].
</pre>

<pre><b>Input: </b>arr[] = [4, 8, 3, 5, 3]<b><br>Output =</b> [2, 2, -1, 2, -1]
<b>Explanation:</b> 
For <b>0th</b> index : here 3 is the smaller, so <b>2(index)</b> 
For <b>1st</b> index : For 8, here 4 & 3 both are
small & at a same distance, so we will pick 3, so <b>2(index)</b>
For <b>2nd</b> index : no tower is smallest, so <b>-1</b>.
For <b>3rd</b> index : For 5, here 3 & 3 both are
small & at a same distance, so we will pick 
<b>3</b>(2nd Index) because it smaller Index, so <b>2(index)
</b>For <b>4th</b> index : no tower is smallest, so <b>-1</b>.
So the final output will be which consistes
Indexes are [2, 2, -1, 2, -1].
</pre>

<b>Constraints:</b><br>1 <= n<= 10<sup>5</sup><br>1 <= arr[i] <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Stack` `Data Structures`
- **Company Tags:** `Atlassian`

### Related Articles
- [Finding Nearest Shortest Tower In Array](https://www.geeksforgeeks.org/finding-nearest-shortest-tower-in-array/)

### Related Interview Experiences
- [Atlassian Interview Experience](https://www.geeksforgeeks.org/atlassian-interview-experience/)
