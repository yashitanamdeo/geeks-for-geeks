<h1 align="center">Frogs and Jumps</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 49.69%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 59K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

<b>N</b> frogs are positioned at one end of the pond. All frogs want to reach the other end of the pond as soon as possible. The pond has some<b> </b>leaves arranged in a straight line. Each frog has the strength to jump exactly <b>K </b>leaves. For example, a  frog having strength 2 will visit the leaves 2, 4, 6, ...  etc. while crossing the pond. 

Given the strength of each frog and the number of leaves, your task is to find the number of leaves that not be visited by any of the frogs when all frogs have reached the other end of the pond. 

<b>Example 1:</b>

<pre><b>Input:</b>
N = 3
leaves = 4
frogs[] = {3, 2, 4} 
<b>Output: </b>1
<b>Explanation:</b>
Leaf 1 will not be visited by any frog.</pre>

<b>Example 2:</b>

<pre><b>Input: </b>
N = 3
leaves = 6
frogs[] = {1, 3, 5} 
<b>Output: </b>0
<b>Explanation: </b>
First frog will visit all the leaves so no 
leaf is left unvisited.</pre>

<b>Your Task:</b><br>
Complete the function <b>unvisitedLeaves</b><b>()</b> which takes the integers <b>N</b>, <b>leaves</b> and the array <b>frogs</b><b> </b>as the input parameters, and returns the number of unvisited leaves.

<b>Expected Time Complexity:</b> O(N*log(leaves))<br>
<b>Expected Auxiliary Space:</b> O(leaves)

<b>Constraints:</b><br>
1 ≤ N, leaves, frogs[i] ≤ 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `sieve` `Data Structures` `Algorithms`
- **Company Tags:** `PayPal`

### Related Articles
- [Count Unvisited Leaves After Frog Jumps](https://www.geeksforgeeks.org/count-unvisited-leaves-after-frog-jumps/)

### Related Interview Experiences
- [Paypal Interview Experience Sde 1 On Campus](https://www.geeksforgeeks.org/paypal-interview-experience-sde-1-on-campus/)
