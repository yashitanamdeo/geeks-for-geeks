<h1 align="center">Coin Change (Count Ways)</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 43.1%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 298K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an integer array <b>coins[ ]</b><b> </b>representing different denominations of currency and an integer <b>sum</b>, find the number of ways you can make <b>sum</b> by using different combinations from coins[ ]. <br><b>Note:</b> Assume that you have an <b>infinite</b> supply of each type of coin. Therefore, you can use any coin as many times as you want.<br>Answers are guaranteed to fit into a 32-bit integer. 

<b>Examples:</b>

<pre><b>Input: </b>coins[] = [1, 2, 3], sum = 4
<b>Output:</b> 4
<b>Explanation</b>: Four Possible ways are: [1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3].
</pre>

<pre><b>Input</b>: coins[] = [2, 5, 3, 6], sum = 10
<b>Output:</b> 5
<b>Explanation</b>: Five Possible ways are: [2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 2, 6], [2, 3, 5] and [5, 5].<br></pre>

<pre><b>Input</b>: coins[] = [5, 10], sum = 3
<b>Output:</b> 0<br><b>Explanation:</b> Since all coin denominations are greater than sum, no combination can make the target sum.</pre>

<b>Constraints:</b><br>1 <= sum <= 10<sup>3</sup><br>1 <= coins[i] <= 10<sup>4</sup><sup><br></sup>1 <= coins.size() <= 10<sup>3</sup>

## Expected Complexities
- Time Complexity: O(n * sum)
- Auxiliary Space: O(sum)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Dynamic Programming` `Data Structures` `Algorithms`
- **Company Tags:** `Paytm` `Flipkart` `Morgan Stanley` `Accolite` `Amazon` `Microsoft` `OYO Rooms` `Samsung` `Snapdeal` `Zoho`

### Related Articles
- [Coin Change Dp 7](https://www.geeksforgeeks.org/coin-change-dp-7/)

### Related Interview Experiences
- [Accolite Interview Experience Set 15 Campus](https://www.geeksforgeeks.org/accolite-interview-experience-set-15-campus/)
- [Paytm Interview Experience Set 4 Walk In Drive](https://www.geeksforgeeks.org/paytm-interview-experience-set-4-walk-in-drive/)
- [Flipkart Interview Experience For Sde 1 On Campus 2019 2](https://www.geeksforgeeks.org/flipkart-interview-experience-for-sde-1-on-campus-2019-2/)
