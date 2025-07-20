<h1 align="center">Paths from root with a specified sum</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 55.0%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 40K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a Binary tree and a sum <b>S</b>, print all the paths, <b>starting from root</b>, that sums upto the given sum. Path <b>not necessarily</b> end on a leaf node.

<b>Example 1:</b>

<pre><b>Input : </b>
sum = 8
Input tree
         1
       /   \
     20      3
           /    \
         4       15   
        /  \     /  \
       6    7   8    9      

<b>Output :</b>
1 3 4
<b>Explanation : </b>
Sum of path 1, 3, 4 = 8.</pre>

<b>Example 2:</b>

<pre><b>Input : </b>
sum = 38<br>Input tree
          10
       /     \
     28       13
           /     \
         14       15
        /   \     /  \
       21   22   23   24
<b>Output :</b>
10 28
10 13 15  
<b>Explanation :</b>
Sum of path 10, 28 = 38 and
Sum of path 10, 13, 15 = 38.</pre>

<b>Your task :</b>
You don't have to read input or print anything. Your task is to complete the function <b>printPaths()</b> that takes the root of the tree and sum as input and returns a vector of vectors containing the paths that lead to the sum.
 
<b>Your Task :</b>
1 <= N <= 2*10<sup>3</sup>
-10<sup>3</sup> <= sum, Node.key <= 10<sup>3</sup>

## Expected Complexities
- Time Complexity: O(n^2)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `Microsoft`

### Related Articles
- [Find Sum Right Leaves Given Binary Tree](https://www.geeksforgeeks.org/find-sum-right-leaves-given-binary-tree/)
- [Print Paths Root Specified Sum Binary Tree](https://www.geeksforgeeks.org/print-paths-root-specified-sum-binary-tree/)
