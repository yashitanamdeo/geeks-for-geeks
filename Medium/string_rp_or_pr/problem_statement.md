<h1 align="center">String rp or pr</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.08%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 34K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string S. In one operation, you can remove the substring "pr" from the string S and get amount X or you can remove the substring "rp" and get the amount Y. <br>
Find the maximum amount you can get if you perform zero or more such operations optimally. 

<b>Note : </b>

- Substring of a string S is defined as a continuous sequence of characters in S.
- After removing pr or rp, the order of remaining letters should remain the same<b>.</b>
<br>
<b>Example 1:</b>

<pre><b>Input:</b>
X = 5, Y = 4
S = "abppprrr"
<b>Output: </b>15
<b>Explanation: </b>
Here, S <b>= "</b>abppprrr" 
X= 5, Y=4.
Remove "pr", new string S = "abpprr".
Remove "pr", new string S = "abpr".
Remove "pr", new string S = "ab".
In total, we removed "pr" 3 times, 
so total score is 3*X + 0*Y = 3*5 =15.
</pre>

 

 

<b>Example 2:</b>

<pre><b>Input:</b>
X = 7, Y = 7
S = "prpptppr"
<b>Output: </b>14
<b>Explanation: </b>
Here, S <b>= "</b>prpptppr" 
X= 7, Y=7.
As both have the same amount we can first 
remove either pr or rp. Here we start with pr
Remove "pr", new string S = "pptppr".
Remove "pr", new string S = "pptp".
In total, we removed "pr" 2 times, 
so total score is 2*X + 0*Y = 2*7 =14.</pre>

<br>
<b>Your Task: </b><br>
You don't need to read input or print anything. Your task is to complete the function<b> solve()</b> which takes the X ,Y and string S as input parameters and returns the maximum amount you can get after performing the above operations.

<br>
<b>Expected Time Complexity:</b> O(|S|)<br>
<b>Expected Auxiliary Space:</b> O(|S|)

<br>
<b>Constraints</b>:<br>
1 ≤ |S| ≤ 10<sup>5</sup><br>
1 ≤ X,Y ≤ 10<sup>5</sup><br>
S contains lowercase English letters only.


<hr>

### Tags
- **Topic Tags:** `Strings` `Greedy` `Stack` `Data Structures` `Algorithms`
- **Company Tags:** `Google`

### Related Articles
- [Maximize Cost Obtained By Removal Of Substrings Pr Or Rp From A Given String](https://www.geeksforgeeks.org/maximize-cost-obtained-by-removal-of-substrings-pr-or-rp-from-a-given-string/)

### Related Interview Experiences
- [Gocc14 Google Online Coding Challenge 2020 New Grad India](https://www.geeksforgeeks.org/gocc14-google-online-coding-challenge-2020-new-grad-india/?ref=rp)
