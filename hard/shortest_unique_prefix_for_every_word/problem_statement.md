<h1 align="center">Shortest Unique prefix for every word</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.02%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 18K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of words, find all shortest unique prefixes to represent each word in the given array. Assume that no word is prefix of another.

<b>Example 1:</b>

<pre><b>Input: 
</b>N = 4
arr[] = {"zebra", "dog", "duck", "dove"}
<b>Output: </b>z dog du dov
<b>Explanation: </b>
z => zebra 
dog => dog 
duck => du 
dove => dov 
</pre>

<b>Example 2:</b>

<pre><b>Input: 
</b>N = 3
arr[] =  {"geeksgeeks", "geeksquiz",
                       "geeksforgeeks"};
<b>Output: </b>geeksg geeksq geeksf
<b>Explanation: </b>
geeksgeeks => geeksg 
geeksquiz => geeksq 
geeksforgeeks => geeksf</pre>

<b>Your task:</b>
You don't have to read input or print anything. Your task is to complete the function <b>findPrefixes()</b> which takes the array of strings and it's size N as input and returns a list of shortest unique prefix for each word 
 
<b>Expected Time Complexity:</b> O(N*length of each word)
<b>Expected Auxiliary Space: </b>O(N*length of each word)
 
<b>Constraints:</b>
1 ≤ N, Length of each word ≤ 1000


<hr>

### Tags
- **Topic Tags:** `Trie` `Advanced Data Structure`
- **Company Tags:** `Microsoft` `Google`

### Related Articles
- [Find All Shortest Unique Prefixes To Represent Each Word In A Given List](https://www.geeksforgeeks.org/find-all-shortest-unique-prefixes-to-represent-each-word-in-a-given-list/)
