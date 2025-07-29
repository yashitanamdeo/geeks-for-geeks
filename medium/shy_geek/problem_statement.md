<h1 align="center">Shy Geek</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.24%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 26K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Geek went to buy some chocolates from a nearby shop with <b>k</b> coins in his pocket. He found that the shop contains <b>n</b> chocolates which are arranged in <b>sorted order (increasing)</b> of their prices.<br><br>Now geek wants to taste costlier chocolates so he decided that <b>he will buy the costliest chocolate</b> (of course among the ones that he can afford) till there exists at least one type of chocolate he can afford. You may assume that there is an infinite supply of chocolates in the shop Geek visited.<br><br>As you know, Geek is a shy person and hence<b> he will enquire about the prices of the chocolates at most 50 times</b> from the shopkeeper. Now, your task is to <b>find the number of chocolates he had enjoyed</b>. <br><br><i><b>Note:</b> If you call the Shop.get function more than 50 times it will return -1. Price of chocolates are pairwise distinct.</i>

<b>Example 1:</b> 

<pre><b>Input:
</b>3 5 
2 4 6

<b>Output:
</b>1

<b>Explanation:</b> The prices of chocolates are [2, 4, 6] and Geek had 5 coins with him. So he can only buy chocolate that costs 4 coins (since he always picks the costliest one).</pre>

<b>Example 2:</b> 

<pre><b>Input:</b>
4 9 
1 2 3 4

<b>Output:
</b>3

<b>Explanation:</b> The prices of chocolates are [1, 2, 3, 4] and Geek had 9 coins with him. So he can buy two chocolates that cost 4 coins. Thereafter, he had only 1 coin with him, hence he will have 1 more chocolate (that costs 1 coin).</pre>

<b>Your Task:</b><br>Return the number of chocolates geeks had eaten. Use the get(int i) function to inquire about the price of the i'th chocolate. <br>Note that, you can only call that function 50 times after which it will return -1. <b>Test cases are generated such that the answer can always be found.</b>

<b>Expected Time Complexity:</b> O(logN)<br><b>Expected Auxiliary Space:</b> O(logN)

<b>Constraints:</b><br>0 < n < 10<sup>5</sup><br>0 < priceOfChocolate < = 10<sup>7 </sup><br>0 < k <= 10<sup>12 </sup>


<hr>

### Tags
- **Topic Tags:** `Binary Search` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Find The Number Of Enjoyable Chocolates For Geeks Budget](https://www.geeksforgeeks.org/find-the-number-of-enjoyable-chocolates-for-geeks-budget/)
