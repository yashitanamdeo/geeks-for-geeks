<h1 align="center">Gadgets of Doraland</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.1%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 8K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

In Doraland, people have unique Identity Numbers called <b>D-id.</b> Doraemon owns the most popular gadget shop in Doraland. Since his gadgets are in high demand and he has only <b>K</b> gadgets left he has decided to sell his gadgets to his most frequent customers only. <b>N</b> customers visit his shop and <b>D-id</b> of each customer is given in an array <b>array[ ]</b>. In case two or more people have visited his shop the same number of time he gives priority to the customer with higher <b>D-id</b>. Find the <b>D-ids</b> of people he sells his <b>K</b> gadgets to.

<b>Example 1:</b>

<pre><b>Input:</b>
N = 6
array[] = {1, 1, 1, 2, 2, 3}
K = 2
<b>Output:</b> 
1 2
<b>Explanation: </b>
Customers with D-id 1 and 2 are most 
frequent.
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N = 8
array[] = {1, 1, 2, 2, 3, 3, 3, 4}
K = 2
<b>Output:</b> 
3 2
<b>Explanation: </b>People with D-id 1 and 2 have 
visited shop 2 times Therefore, in this 
case, the answer includes the D-id 2 as 2 > 1.</pre>

<b>Your Task:</b><br>
You don't need to read input or print anything. Complete the function <b>TopK() </b>which takes <b>array[ ]</b> and integer <b>K</b> as input parameters and returns an array containing <b>D-id</b> of customers he has decided to sell his gadgets to.

<b>Expected Time Complexity:</b> O(N)<br>
<b>Expected Auxiliary Space:</b> O(N)

<b>Constraints:</b><br>
1 ≤ N ≤ 10<sup>5</sup><br>
1 ≤ D-id ≤ 10<sup>4</sup>


<hr>

### Tags
- **Topic Tags:** `Hash` `Heap` `Data Structures`
- **Company Tags:** `None`
