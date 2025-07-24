<h1 align="center">Cake Distribution Problem</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 64.62%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 22K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Geek is organizing a birthday party, so his friends brought a cake for him. The cake consists of <b>N</b> chunks, whose individual sweetness is represented by the<b> sweetness </b>array.<b> </b>Now at the time of distribution, Geek cuts the cake into <b>K + 1</b> pieces to distribute among his <b>K</b> friends. One piece he took for himself. Each piece consists of some consecutive chunks. He is very kind, so he left the piece with <b>minimum</b> sweetness for him.

You need to find the <b>maximum</b> sweetness that the Geek can get if he distributes the cake optimally.

<b>Example 1:</b>

<pre><b>Input:</b>
N  = 6, K = 2
sweetness[] = {6, 3, 2, 8, 7, 5}
<b>Output:</b>
9
<b>Explanation:</b>
Geek can divide the cake to [6, 3], [2, 8], [7, 5] 
with sweetness level 9, 10 and 12 respectively.
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N  = 7, K = 3
sweetness[] = {1, 2, 4, 7, 3, 6, 9}
<b>Output:</b>
7
<b>Explanation:</b>
Geek can divide the cake to [1, 2, 4], [7], [3, 6], [9] 
with sweetness level 7, 7, 9 and 9 respectively.</pre>

<b>Your Task:</b><br>
You need to complete the <b>maxSweetness()</b> function which takes an integer array of <b>sweetness</b>, an integer <b>N</b> and an integer <b>K</b> as the input parameters and returns an integer denoting the maximum sweetness that the Geek can get.

<b>Expected Time Complexity:</b> O(NlogM), where M is the sum of elements in the array.<br>
<b>Expected Space Complexity:</b> O(1)

<b>Constraints:</b><br>
1 <= N <= 10<sup>5</sup><br>
0 <= K < N<br>
1 <= sweetness[i] <= 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Binary Search` `Arrays`
- **Company Tags:** `None`
