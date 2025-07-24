<h1 align="center">Min distance between two given nodes of a Binary Tree</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 39.13%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 129K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary tree with <b>n</b> nodes and two node values, <b>a</b> and <b>b</b>, your task is to find the minimum distance between them. The given two nodes are guaranteed to be in the binary tree and all node values are <b>unique</b>.<br>

<b>Examples :</b>

<pre><b>Input: </b>Tree = [1, 2, 3]<b>
        </b>1
      /  \
     2    3
a = 2, b = 3
<b>Output: </b>2<b>
Explanation: </b>We need the distance between 2 and 3. Being at node 2, we need to take two steps ahead in order to reach node 3. The path followed will be: 2 -> 1 -> 3. Hence, the result is 2. </pre>

<pre><b>Input: </b>Tree = [11, 22, 33, 44, 55, 66, 77]<b>
        </b>11
      /   \
     22  33<br>    /  \  /  \<br>  44 55 66 77
a = 77, b = 22
<b>Output: </b>3<b>
Explanation: </b>We need the distance between 77 and 22. Being at node 77, we need to take three steps ahead in order to reach node 22. The path followed will be: 77 -> 33 -> 11 -> 22. Hence, the result is 3.<br></pre>

<pre><b>Input: </b>Tree = [1, 2, 3]<b>
        </b>1
      /  \
     2    3
a = 1, b = 3
<b>Output: </b>1</pre>

<b>Constraints:</b><br>2 <= number of nodes <= 10<sup>5</sup><br>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(Height of the Tree)

<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `Amazon` `Samsung` `MakeMyTrip` `Ola Cabs` `Linkedin` `Qualcomm`

### Related Articles
- [Find Distance Between Two Nodes Of A Binary Tree](https://www.geeksforgeeks.org/find-distance-between-two-nodes-of-a-binary-tree/)

### Related Interview Experiences
- [Qualcomm Interview Experience Set 8 Experienced](https://www.geeksforgeeks.org/qualcomm-interview-experience-set-8-experienced/)
- [Samsung Research Institute Bangalore Srib Intern](https://www.geeksforgeeks.org/samsung-research-institute-bangalore-srib-intern/)
- [Samsung R D Banglore Intern Interview Experience](https://www.geeksforgeeks.org/samsung-r-d-banglore-intern-interview-experience/)
- [Samsung Bangalore Internship Interview Experience 2018](https://www.geeksforgeeks.org/samsung-bangalore-internship-interview-experience-2018/)
- [Samsung R D Bangalore Internship Experience 2018](https://www.geeksforgeeks.org/samsung-r-d-bangalore-internship-experience-2018/)
- [Samsung Srib Internship Interview Experience August 2018](https://www.geeksforgeeks.org/samsung-srib-internship-interview-experience-august-2018/)
