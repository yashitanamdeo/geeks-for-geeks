<h1 align="center">Transfiguration</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 36.72%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 21K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Professor McGonagall teaches transfiguration at Hogwarts. She has given Harry the task of changing himself into a cat. She explains that the trick is to analyze your own DNA and change it into the DNA of a cat. The transfigure spell can be used to pick any one character from the DNA string, remove it and insert it in the beginning. <br>
Help Harry calculates minimum number of times he needs to use the spell to change himself into a cat.

<b>Example 1:</b>

<pre><b>Input: 
</b>A = "GEEKSFORGEEKS" 
B = "FORGEEKSGEEKS"
<b>Output:</b> 3
<b>Explanation:</b>The conversion can take place 
in 3 operations:
1. Pick 'R' and place it at the front, 
   A="RGEEKSFOGEEKS"
2. Pick 'O' and place it at the front, 
   A="ORGEEKSFGEEKS"
3. Pick 'F' and place it at the front, 
   A="FORGEEKSGEEKS"</pre>

<b>Example 2:</b>

<pre><b>Input: 
</b>A = "ABC" 
B = "BCA"
<b>Output:</b> 2
<b>Explanation:</b> The conversion can take place 
in 2 operations:
1. Pick 'C' and place it at the front, 
   A = "CAB"
2. Pick 'B' and place it at the front, 
   A = "BCA"
</pre>

<b>Your Task: </b> <br>
You don't need to read input or print anything. Complete the function <b>transfigure()</b> which takes strings <b>A</b> and <b>B</b> as input parameters and returns the minimum number of spells needed. If it is not possible to convert <b>A</b> to <b>B</b> then return -1.

<b>Expected Time Complexity:</b> O(max(|A|, |B|))<br>
<b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>
1 ≤ |A|, |B| ≤ 10<sup>5</sup><br>
A and B consists of lowercase and uppercase letters of english alphabet only.


<hr>

### Tags
- **Topic Tags:** `Hash` `Strings` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Transform One String To Another Using Minimum Number Of Given Operation](https://www.geeksforgeeks.org/transform-one-string-to-another-using-minimum-number-of-given-operation/)
