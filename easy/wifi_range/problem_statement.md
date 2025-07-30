<h1 align="center">Wifi Range</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.63%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 33K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There are <b>N</b> rooms in a straight line in Geekland State University's hostel, you are given a binary string <b>S</b> of length <b>N</b> where <b>S[i] = '1'</b> represents that there is a wifi in <b>i<sup>th</sup></b> room or <b>S[i] = '0'</b> represents no wifi. Each wifi has range <b>X</b> <i>i.e.</i> if there is a wifi in i<sup>th</sup> room then its range will go upto <b>X</b> more rooms on its left as well as right. You have to find whether students in all rooms can use wifi.

<b>Example 1: </b>

<pre><b>Input:</b>
N = 3, X = 0
S = "010"
<b>Output:</b>
0
<b>Explanation</b>: 
Since the range(X)=0, So Wifi is only 
accessible in second room while 1st & 3rd
room have no wifi.
</pre>

<b>Example 2: </b>

<pre><b>Input:</b>
N = 5, X = 1
S = "10010"
<b>Output:</b>
1
<b>Explanation</b>: 
Index 0 : Wifi is available
Index 1 : Since range of 0th Index is 1
          so, here wifi will be available.
Index 2 : Since range of 3rd Index is 1
          so, here also wifi available.
Index 3 : Wifi is available
Index 4 : here range of 3rd Index is available.
So all the rooms have wifi, so return true.
</pre>

<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>wifiRange( )</b> which takes integer <b>N</b>, string <b>S</b> and integer <b>X</b> as input parameters and returns true if students in all rooms can use wifi or false otherwise.

<b>Expected Time Complexity</b>:O(N)<br>
<b>Expected Space Complexity</b>:O(1)

<b>Constraints:</b><br>
1 ≤ N ≤ 10<sup>6</sup><br>
0 ≤ X ≤ 10<sup>6</sup>


<hr>

### Tags
- **Topic Tags:** `Strings` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Hostel Wifi Range Problem](https://www.geeksforgeeks.org/hostel-wifi-range-problem/)
