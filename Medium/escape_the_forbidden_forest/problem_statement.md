<h1 align="center">Escape the Forbidden Forest</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 57.29%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 6K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Penelope and her classmates are lost in the Forbidden Forest and the Devil is out to get them. But Penelope has magical powers that can build bridges across the dangerous river and take her friends to safety. The only bridges that can withstand the Devil's wrath are the ones built between two similar trees in the forest. <br>
Given str1 and str2 denoting the order of trees on either side of the river, find the maximum number of bridges that Penelope can build and save everyone from the Devil. <br>
<b>Note: </b>Each tree in the forest belongs to one of the 3 categories represented by * or # or @, and it's easy to understand that bridges do not intersect or cross each other. 

<b>Example 1:</b>

<pre><b>Input:</b>
str1 = "*@#*" 
str2 = "*#"
<b>Output:</b>
2
<b>Explanation:</b>
str1 = "*@#*" and str2 = "*#" 
Two bridges can be built between the banks 
of the river in the following manner. 
* @ # *
|   |
*   #</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
str1 = "***"
str2 = "##"
<b>Output:</b>
0
</pre>

<b>Your Task:</b><br>
You don't need to read input or print anything. Complete the function <b>build_bridges()</b> that takes str1 and str2 as input parameters and returns the maximum number of bridges that can be built. 

<b>Expected Time Complexity:</b> O(N*M)<br>
<b>Expected Auxiliary Space:</b> O(N*M)

<b>Constraints:</b><br>
1 ≤ N, M ≤ 100<br>
Where, N and M are the size of the string str1 and str2 respectively.


<hr>

### Tags
- **Topic Tags:** `Strings` `Dynamic Programming` `Data Structures` `Algorithms`
- **Company Tags:** `None`
