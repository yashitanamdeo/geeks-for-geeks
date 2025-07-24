<h1 align="center">Remove leading zeros from an IP address</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 48.03%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 12K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an IP address, remove leading zeros from the IP address. Note that our IP address here can be a little different. It can have numbers greater than 255. Also, it does not necessarily have 4 numbers. The count can be lesser/more.

<b>Example 1:</b>

<pre><b>Input:</b>
S = "100.020.003.400"
<b>Output:</b> 100.20.3.400
<b>Explanation</b>: The leading zeros are removed
from 20 and 3.
</pre>

<b>Example 2:</b>

<pre><b>Input</b>: 
S = "100.000.010.0999"
<b>Output:</b> 100.0.10.999
<b>Explanation</b>: The leading zeros are removed
from 0, 10 and 999.
</pre>

<br>
<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>newIPAdd() </b>which takes the string S representing the IP address as input and returns a string representing the resultant IP address. 

<br>
<b>Expected Time Complexity: </b>O(|S|).<br>
<b>Expected Auxiliary Space: </b>O(|S|).

<br>
<b>Constraints:</b><br>
1<=|S|<=1000


<hr>

### Tags
- **Topic Tags:** `Strings` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Python Remove Leading Zeros Ip Address](https://www.geeksforgeeks.org/python-remove-leading-zeros-ip-address/)
