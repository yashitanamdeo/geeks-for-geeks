<h1 align="center">Killing Spree</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 48.32%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 13K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There are Infinite People Standing in a row, indexed from 1.<br>A person having index 'i' has strength of (i*i).<br>You have Strength 'P'. You need to tell what is the maximum number of People You can Kill With your Strength P.<br>You can only Kill a person with strength 'X' if P >= 'X'  and after killing him, Your Strength decreases by 'X'. <br> 

<b>Example 1:</b>

<pre><b>Input</b>:
N = 14
<b>Output:</b> 3
<b>Explanation</b>:
The strengths of people is 1, 4, 9, 16, .... 
and so on. WE can kill the first 3 person , 
after which our Power becomes 0 and we cant 
kill anyone else. So answer is 3
</pre>

 

<b>Example 2:</b>

<pre><b>Input:</b>
N = 10
<b>Output: </b>2
</pre>

<br><b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>killinSpree()</b> which takes the integer N as input parameters and returns the maximum Number of People You can kill.<br><br><b>Expected Time Complexity:</b> O(log(n))<br><b>Expected Auxiliary Space:</b> O(1)

 

<b>Constraints:</b><br>1 ≤ T ≤ 10<sup>3</sup><br>1 ≤ N ≤ 10<sup>12</sup>


<hr>

### Tags
- **Topic Tags:** `Mathematical` `Divide and Conquer` `Binary Search` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Maximum Number Of People That Can Be Killed With Strength P](https://www.geeksforgeeks.org/maximum-number-of-people-that-can-be-killed-with-strength-p/)
