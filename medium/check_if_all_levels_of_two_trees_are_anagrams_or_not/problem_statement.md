<h1 align="center">Check if all levels of two trees are anagrams or not</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 56.88%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 22K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two binary trees with same number of nodes, the task is to check if each of their levels are anagrams of each other or not. 

<b>Example 1:</b>

<pre><b>Input:</b>
<img src="https://media.geeksforgeeks.org/img-practice/abc-1649622345.gif" alt="" title=""/>
<b>Output: </b>1
<b>Explanation:</b> 
<b>Tree 1:</b>
Level 0 : 1
Level 1 : 3, 2
Level 2 : 5, 4

<b>Tree 2:</b>
Level 0 : 1
Level 1 : 2, 3
Level 2 : 4, 5

As we can clearly see all the levels of above two binary trees 
are anagrams of each other, hence return true.
</pre>

<b>Example 2:</b>

<pre><b>Input:
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20221119111710/WhatsAppImage20221119at111602AM.jpeg" alt="" title=""/>
Output: 0</b>
<b>Explanation:</b> 
<b>Tree 1:
</b>Level 0 : 1
Level 1 : 2, 3 
Level 2 : 5, 4 

<b>Tree 2:</b> 
Level 0 : 1 
Level 1 : 2, 4 
Level 2 : 5, 3 

As we can clearly see that level 1 and leve 2 are not anagrams of each other, hence return false.
</pre>

<b>Your Task:  </b><br>
You don't need to read input or print anything. Your task is to complete the function <b>areAnagrams</b><b>()</b> which takes the root of two trees as input and returns an 1 if all the levels are anagrams, else returns 0 as output.<br>
 

<b>Expected Time Complexity:</b> O(NlogN)<br>
<b>Expected Auxiliary Space:</b> O(N)

 

<b>Constraints:</b><br>
1 <= N <= 10<sup>4</sup><br>
1 <= tree.val <= 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Check If All Levels Of Two Trees Are Anagrams Or Not](https://www.geeksforgeeks.org/check-if-all-levels-of-two-trees-are-anagrams-or-not/)
