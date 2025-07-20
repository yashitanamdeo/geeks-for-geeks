<h1 align="center">Leaf under budget</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.05%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 47K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary tree and a <b>budget</b>. Assume you are at the root of the tree<b>(level 1)</b>, you need to maximise the count of leaf nodes you can visit in your budget if the <b>cost of visiting </b>a leaf node is equal to the <b>level of that leaf node</b>. 

<b>Example 1:</b>

<pre><b>Input: </b>
                  10
                /    \
               8      2
             /      /   \
            3      3     6
                    \
                     4
and budget = 8
<b>Output: 2</b>
<b>Explanation:</b>
Cost For visiting Leaf Node 3: 3
Cost For visiting Leaf Node 4: 4
Cost For visiting Leaf Node 6: 3
In budget 8 one can visit Max 2 Leaf Nodes.</pre>

<b>Example 2:</b>

<pre><b>Input: </b>
         1
       /   \
      2     3
     / \   / \
    4   5 6   7
and budget = 5
<b>Output: </b>1<br><b>Explanation:</b> We can only visit either node 4 or 5.</pre>

<b>Your Task:</b>

You don't need to read input or print anything. Your task is to complete the function <b>getCount() </b>which takes root node of the tree and a integer denoting the budget as input parameters and returns an integer denoting the count of visited leaf nodes of the tree.

<b>Expected Time Complexity:</b> O(N)<br><b>Expected Auxiliary Space:</b> O(N)

<b>Constraints:</b><br>1<=N<=10<sup>5</sup><br>1<=budget<=10<sup>4</sup>


<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `Oracle`

### Related Articles
- [Maximum Number Of Leaf Nodes That Can Be Visited Within The Given Budget](https://www.geeksforgeeks.org/maximum-number-of-leaf-nodes-that-can-be-visited-within-the-given-budget/)

### Related Interview Experiences
- [Oracle Interview Experience Set 52 Campus Application Engineer](https://www.geeksforgeeks.org/oracle-interview-experience-set-52-campus-application-engineer/)
