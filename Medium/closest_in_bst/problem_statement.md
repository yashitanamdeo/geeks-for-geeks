<h1 align="center">Closest in BST</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 47.51%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 84K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a <b>[BST](http://quiz.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/)</b> and an integer. Find the least absolute difference between any node value of the BST and the given integer.

<b>Example 1:</b>

<pre><b>Input:
</b>        10
      /   \
     2    11
   /  \ 
  1    5
      /  \
     3    6
      \
       4
K = 13
<b>Output: </b>2<b>
Explanation: </b>K=13. The node that has value nearest to K is 11. so the answer is 2
</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>      8
    /   \
   1     9
    \     \
     4    10
    /
   3
K = 9
<b>Output: </b>0<b>
Explanation: </b>K=9. The node that has value nearest to K is 9. so the answer is 0.</pre>

<b>Constraints:</b><br>1 <= Number of nodes <= 10<sup>5<br></sup>1 <= Value stored at nodes(data), K <= 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(h)
- Auxiliary Space: O(h)

<hr>

### Tags
- **Topic Tags:** `Binary Search Tree` `Tree` `Data Structures`
- **Company Tags:** `Amazon` `MAQ Software`

### Related Articles
- [Find Closest Element Binary Search Tree](https://www.geeksforgeeks.org/find-closest-element-binary-search-tree/)

### Related Interview Experiences
- [Maq Software Interview Experience Set 7](https://www.geeksforgeeks.org/maq-software-interview-experience-set-7/)
