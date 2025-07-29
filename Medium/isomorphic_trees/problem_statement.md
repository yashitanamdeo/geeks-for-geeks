<h1 align="center">Isomorphic Trees</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 49.11%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 113K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two Binary Trees. Check whether they are Isomorphic or not.

<b>Note: </b><br>Two trees are called isomorphic if one can be obtained from another by a series of flips, i.e. by swapping left and right children of several nodes. Any number of nodes at any level can have their children swapped. Two empty trees are isomorphic.<br>For example, the following two trees are isomorphic with the following sub-trees flipped: 2 and 3, NULL and 6, 7 and 8.<br>[<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/ISomorphicTrees-e1368593305854.png" alt="ISomorphicTrees" title="" width="397" height="163"/>](https://media.geeksforgeeks.org/wp-content/cdn-uploads/ISomorphicTrees-e1368593305854.png)

<b>Examples:</b>

<pre><b>Input: </b>root1[] = [1, 2, 3, 4, 5, 7, 6, N, 7, 8], root2[] = [1, 3, 2, N, 6, 4, 5, 8, 7]<b><br></b>
<a href="https://media.geeksforgeeks.org/wp-content/cdn-uploads/ISomorphicTrees-e1368593305854.png"><img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/ISomorphicTrees-e1368593305854.png" alt="ISomorphicTrees" title="" width="397" height="163"/></a><b>
Output: </b>true</pre>

<pre><b>Input:</b> root1[] = [1, 2, 3, 4], root2[] = [1, 3, 2, 4]<br>     1            1  <br>    / \          /    \  <br>  2    3      3       2  <br> /           /  <br>4<b>          </b>4<b><br>Output: </b>false</pre>

<pre><b>Input: </b>root1[] = [1, 2, 3, 4], root2[] = [1, 3, 2, N, N, N, 4]<b><br></b>
     1           1
    /  \         /   \
   2    3      3     2
  /                    \
 4<b>                        </b>4<b>
Output: </b>true</pre>

<b>Constraints:</b><br>1<=number of nodes<=10<sup>5<br></sup>1<= node->data <=10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `Amazon` `Microsoft`

### Related Articles
- [Tree Isomorphism Problem](https://www.geeksforgeeks.org/tree-isomorphism-problem/)

### Related Interview Experiences
- [Amazon Interview Experience Set 332 Off Campus](https://www.geeksforgeeks.org/amazon-interview-experience-set-332-off-campus/ )
- [Microsoft Interview Set 33 Campus Internship](https://www.geeksforgeeks.org/microsoft-interview-set-33-campus-internship/)
- [Amazon Interview Set 14 2]( http://www.geeksforgeeks.org/amazon-interview-set-14-2/)
