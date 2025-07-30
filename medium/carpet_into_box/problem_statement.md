<h1 align="center">Carpet into Box</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.52%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 24K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There is a carpet of a size a*b [length * breadth]. You are given a box of size c*d. The task is, one has to fit the carpet in the box in a minimum number of moves. 

<b>In one move, you can either decrease the length or the breadth of the carpet by half (floor value of its half).</b>

Note: One can even turn the carpet by 90 degrees any number of times, wont be counted as a move.

 

<b>Example 1:</b>

<pre><b>Input:</b>
A = 8, B = 13
C = 6, D = 10
<b>Output:</b>
Minimum number of moves: 1
<b>Explanation:</b>
Fold the carpet by breadth, 13/2 i.e. 6, 
so now carpet is 6*8 and can fit fine.
</pre>

 

<b>Example 2:</b>

<pre><b>Input:
</b>A = 4, B = 8
C = 3, D = 10
<b>Output:
</b>Minimum number of moves: 1
<b>Explanation:</b> Fold the carpet by length , 4/2 i.e. 2,
so now carpet is 2*8 and can fit fine.
</pre>

 

<b>Your Task:</b><br>
You don't need to read input or print anything. You only need to complete the function<b> carpetBox() </b>that takes an integer A, B, C and D as input and returns an integer denoting the minimum numbers of moves required to fit the carpet into the box.

 

<b>Expected Time Complexity: </b>O( max( log(a), log(b) ) ) .<br>
<b>Expected Auxiliary Space: </b>O(1) .

 

<b>Constrains:</b><br>
1<= A,B,C,D <= 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Mathematical` `Algorithms`
- **Company Tags:** `Nutanix`

### Related Articles
- [Minimize Steps To Fit The Carpet In Box By Halving Its Sides](https://www.geeksforgeeks.org/minimize-steps-to-fit-the-carpet-in-box-by-halving-its-sides/)

### Related Interview Experiences
- [Nutanix Interview Experience 2018](https://www.geeksforgeeks.org/nutanix-interview-experience-2018/)
