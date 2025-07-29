<h1 align="center">Lemonade Change</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 52.02%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 46K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are an owner of lemonade island, each lemonade costs <b>$5</b>. Customers are standing in a queue to buy from you and order one at a time (in the order specified by given array <b>bills[]</b>). Each customer will only buy one lemonade and pay with either a <b>$5</b>, <b>$10</b>, or<b> $20 </b>bill. You must provide the correct change to each customer so that the net transaction is that the customer pays <b>$5</b>.

<b>NOTE: </b>At first, you do not have any bill to provide changes with. You can provide changes from the bills that you get from the previous customers.

Given an integer array <b>bills</b> of size <b>N</b> where <b>bills [ i ]</b> is the bill the <b>i</b><sup><b>th</b> </sup>customer pays, return<b> true</b> if you can provide every customer with the correct change, or <b>false</b> otherwise.

<b>Example 1:</b>

<pre><b>Input:</b><br>N = 5<br>bills [ ] = {5, 5, 5, 10, 20}<br><b>Output: </b>True<br><b>Explanation:</b> <br>From the first 3 customers, we collect three $5 bills in order.<br>From the fourth customer, we collect a $10 bill and give back a $5.<br>From the fifth customer, we give a $10 bill and a $5 bill.<br>Since all customers got correct change we return true.</pre>

 

<b>Example 2:</b>

<pre><b>Input:</b><br>N = 5<br>bills [ ] = {5, 5, 10, 10, 20}<br><b>Output: </b>False<br><b>Explanation:</b> <br>From the first two customers in order, we collect two $5 bills.<br>For the next two customers in order, we collect a $10 bill and give back a $5 bill.<br>For the last customer, we can not give the change of $15 back because we only have two $10 bills.<br>Since not every customer received the correct change, the answer is false.</pre>

 

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>lemonadeChange()</b> which takes the interger <b>N</b> and integer array <b>bills</b> <b>[ ] </b>as parameters and returns true if it is possible to provide change to every customer otherwise false.

<b>Expected Time Complexity:</b> O(N)<br><b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>1 ≤ N ≤ 10<sup>5</sup><br>bills[i] contains only {5, 10, 20}


<hr>

### Tags
- **Topic Tags:** `Arrays` `Greedy` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Lemonade Stand Change Challenge](https://www.geeksforgeeks.org/lemonade-stand-change-challenge/)
