<h1 align="center">Maximum Diamonds</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.4%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 48K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There are  bags with diamonds in them. The i'th of these bags contains <b>arr[i] </b>diamonds. If you drop a bag with <b>arr[i]</b> diamonds, it changes to <b>arr[i]/2 </b>diamonds and you gain <b>arr[i] </b>diamonds. Dropping a bag takes 1 minute. Find the <b>maximum number of diamonds</b> that you can take if you are given <b>k </b>minutes.

<b>Examples:</b>

<pre><b>Input:</b>arr[]<b>= </b>[2, 1, 7, 4, 2], k = 3<b><br></b><b>Output: </b>14
<b>Explanation:</b>
The state of bags is:2 1 7 4 2
Take all diamonds from Third bag (7).
State of bags becomes: 2 1 3 4 2 
Take all diamonds from Fourth bag (4).
State of bags becomes: 2 1 3 2 2
Take all diamonds from Third bag (3).<br>State of bags becomes: 2 1 1 2 2 
Hence,number of Diamonds = 7+4+3 = 14.</pre>

<pre><b>Input:</b>arr[]<b>=</b>[7, 1, 2], k = 2
<b>Output:</b>10
<b>Explanation:<br></b>Take all diamonds from First bag (7).<br>State of bags becomes: 3 1 2 <br>Take all diamonds from again First bag (3).<br>State of bags becomes: 1 1 2<br>You can take a <b>maximum </b>of 10 diamonds.
</pre>

<b>Constraints:</b><br>1 ≤ n≤ 10<sup>5<br></sup>0 ≤  k, arr[i] ≤ 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Mathematical` `STL` `Data Structures` `Algorithms` `Heap`
- **Company Tags:** `None`

### Related Articles
- [Maximum Number Of Diamonds That Can Be Gained In K Minutes](https://www.geeksforgeeks.org/maximum-number-of-diamonds-that-can-be-gained-in-k-minutes/)
