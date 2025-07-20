<h1 align="center">Theft at World Bank</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 39.58%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 8K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

The worlds most successful thief Albert Spaggiari was planning for his next heist on the world bank. He decides to carry a sack with him, which can carry a maximum weight of <b>c</b> kgs. Inside the world bank there were <b>n</b> large blocks of gold. All the blocks have some profit value associated with them<i> i.e.</i> if he steals <b>i<sup>th</sup></b> block of weight <b>w[i]</b> then he will have <b>p[i] </b>profit. As blocks were heavy he decided to steal some part of them by cutting them with his cutter.<br>The thief does not like symmetry, hence, he wishes to not take blocks or parts of them whose weight is a perfect square. Now, you need to find out the maximum profit that he can earn given that he can only carry blocks of gold in his sack. 

<b>Note</b>: The answer should be precise upto 3 decimal places.

 

<b>Examples :</b>

<pre>n = 3, c = 10, w[] = {4, 5, 7}, p[] = {8, 5, 4)
<b>Output: </b>
7.857
<b>Explanation: </b>As first blocks weight is 4 which is a perfect square, he will not use this block. Now with the remaining blocks the most optimal way is to use 2<sup>nd</sup> block completely and cut 5kg piece from the 3<sup>rd</sup> block to get a total profit of 5 + 2.857 = 7.857</pre>

<b>Expected Time Complexity: </b>O(n * Log(n))<br><b>Expected Space Complexity : </b>O(n)

<b>Constraints:</b><br>1 ≤ n ≤ 10<sup>3</sup><br>1 ≤ c ≤ 10<sup>18</sup><br>1 ≤ w<sub>i </sub>≤ 10<sup>9</sup><br>1 ≤ p<sub>i </sub>≤ 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Greedy` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Theft At World Bank](https://www.geeksforgeeks.org/theft-at-world-bank/)
