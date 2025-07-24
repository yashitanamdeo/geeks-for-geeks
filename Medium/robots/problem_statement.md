<h1 align="center">Robots</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 43.01%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 7K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There are two kinds of bots <b>A</b> and <b>B</b> in a <b>1-D</b> array. <b>A</b> bot can only move left while <b>B</b> can only move right. There are also empty spaces in between represented by <b>#</b>. But its also given that the bots cannot cross over each other. 

Given the initial state and final state, we should tell if the transformation is possible.

<b>NOTE: </b>There can be many bots of the same type in a particular array. 

<br>
<b>Example 1:</b>

<pre><b>Input</b>:
s1 = #B#A#
s2 = ##BA#
<b>Output:</b> Yes
<b>Explanation</b>: Because we can reach the 
final state by moving 'B' to the 
right one step.
</pre>

<br>
<b>Example 2:</b>

<pre><b>Input:</b>
s1 = #B#A#
s2 = #A#B# 
<b>Output:</b> No
<b>Explanation</b>: Because the robots 
cannot cross each other.</pre>

<br>
<br>
<b>Your Task:  </b><br>
You don't need to read input or print anything. Your task is to complete the function <b>moveRobots()</b> which takes the initial and final states as strings <b>s1 </b>and <b>s2 </b>respectively and returns if a valid transformation can be done. Return "Yes" if possible, else "No".<br>
<br>
 

<b>Expected Time Complexity:</b> O(|s1|)<br>
<b>Expected Auxiliary Space:</b> O(|s1|)<br>
<br>
 

<b>Constraints:</b><br>
1 <= <b>|</b>s1<b>|</b> = <b>|</b>s2<b>|</b> <= 10<sup>5</sup><br>
The strings only consists of 'A', 'B' and '#'.


<hr>

### Tags
- **Topic Tags:** `implementation`
- **Company Tags:** `Ola Cabs`

### Related Articles
- [Convert String S1 To S2 By Moving B To Right And A To Left Without Crossover](https://www.geeksforgeeks.org/convert-string-s1-to-s2-by-moving-b-to-right-and-a-to-left-without-crossover/)

### Related Interview Experiences
- [Ola Interview Experience Set 15 1 Year Experienced For Sde1](https://www.geeksforgeeks.org/ola-interview-experience-set-15-1-year-experienced-for-sde1/)
