<h1 align="center">Min Coin</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 31.88%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 32K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a list of coins of <b>distinct denominations arr</b> and the <b>total amount of money</b>. Find the<b> minimum number of coins</b> required to make up that amount. Output<b> -1</b> if that money cannot be made up using given coins.<br>You may assume that there are<b> infinite </b>numbers of coins of each type.<br> 

<b>Example 1:</b>

<pre><b>Input: </b>arr = [1, 2, 5], amount = 11
<b>Output: </b>3
<b>Explanation: </b>2*5 + 1 = 11. So taking 2 
denominations of 5 and 1 denomination of  
1, one can make 11.
</pre>

<b>Example 2:</b>

<pre><b>Input: </b>arr = [2, 6], amount = 7
<b>Output: </b>-1
<b>Explanation: </b>Not possible to make 7 using 
denominations 2 and 6.
</pre>

 

<b>Your Task:</b><br>You don't need to read or print anything. Your task is to complete the function <b>MinCoin()</b> which takes a list of denominations and amounts as input parameters and returns a minimum number of coins to make up the amount. If not possible returns -1.<br> 

<b>Expected Time Complexity: </b>O(n*amount)<br><b>Expected Space Complexity: </b>O(amount)<br> 

<b>Constraints:</b><br>1 <= number of distinct denominations <= 100<br>1 <= amount,<b>arri</b> <= 10<sup>4</sup>


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Greedy` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Find Minimum Number Of Coins That Make A Change](https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/)
