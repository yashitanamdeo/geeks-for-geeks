<h1 align="center">Shop in Candy Store</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 45.43%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 83K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

In a candy store, there are different types of candies available and <b>arr</b><b>[i]</b> represent the price of  i<sup>th</sup> types of candies. You are now provided with an attractive offer.<br>For every candy you buy from the store and get <b>k</b> other candies ( all are different types ) for free. Now you have to answer two questions, what is the <b>minimum </b>and<b> maximum amount of money</b> you have to spend to buy all the<b> </b> candies.<br>In both the cases you must utilize the offer i.e. you buy one candy and get <b>k </b>other candies for free.

<b>Examples : <br></b>

<pre><b>Input: </b>arr[] = [3, 2, 1, 4], k = 2<br><b>Output: </b>[3, 7]<br><b>Explanation: </b>As according to the offer if you buy one candy you can take at most two more for free. So in the first case, you buy the candy worth 1 and takes candies worth 3 and 4 for free, also you need to buy candy worth 2. So <b>min cost</b>: 1+2 = 3. In the second case, you can buy the candy worth 4 and takes candies worth 1 and 2 for free, also you need to buy candy worth 3. So <b>max cost:</b> 3+4 = 7.</pre>

<pre><b>Input:</b> arr[] = [3, 2, 1, 4, 5], k = 4<b>
Output:</b> [1, 5]
<b>Explanation: </b>For minimimum cost buy the candy with the cost 1 and get all the other candies for free. For maximum cost buy the candy with the cost 5 and get all other candies for free.
</pre>

<b>Constraints:</b><br>1 ≤ arr.size()<b> </b>≤ 10<sup>5</sup><br>0 ≤ k ≤ arr.size()<br>1 ≤ arr[i] ≤ 10<sup>4</sup>

## Expected Complexities
- Time Complexity: O(n log n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Greedy` `Sorting` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Find Minimum Maximum Amount Buy N Candies](https://www.geeksforgeeks.org/find-minimum-maximum-amount-buy-n-candies/)
