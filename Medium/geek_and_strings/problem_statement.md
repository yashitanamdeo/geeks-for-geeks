<h1 align="center">Geek and Strings</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 58.11%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 16K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Geek has a list Li containing (not necessarily distinct) N words and Q queries. Each query consists of a string x. For each query, find how many strings in the List Li has the string x as its prefix. 

<br>
<b>Example 1:</b>

<pre><b>Input: </b>
N = 5, Q = 5
li[] = {'abracadabra', 'geeksforgeeks', 
      'abracadabra', 'geeks', 'geeksthrill'}
query[] = {'abr', 'geeks', 'geeksforgeeks', 
         'ge', 'gar'}

<b>Output:</b> 2 3 1 3 0

<b>Explaination: </b>
<b>Query 1: </b>The string 'abr' is prefix of 
two 'abracadabra'. 
<b>Query 2: </b>The string 'geeks' is prefix of three 
strings 'geeksforgeeks', 'geeks' and 'geeksthrill'. 
<b>Query 3: </b>The string 'geeksforgeeks' is prefix 
of itself present in li. 
<b>Query 4: </b>The string 'ge' also is prefix of three 
strings 'geeksforgeeeks', 'geeks', 'geeksthrill'. 
<b>Query 5: </b>The string 'gar' is not a prefix of any 
string in li.</pre>

<br>
<b>Your Task:</b><br>
You do not need to read input or print anything. Your task is to complete the function <b>prefixCount() </b>which takes N, Q, li[] and query[] as input parameters and returns a list containing the count of prefixes for each query. 

<br>
<b>Expected Time Complexity:</b> O(Q*x) + O(N*L) Where Q is the number of queries, x is the longest word in the query, N = number of words inserted in Trie and L = length of longest word inserted in Trie.<br>
<b>Expected Auxiliary Space:</b> O(N*List [i])

<br>
<b>Constraints:</b><br>
1 ≤ N ≤ 3 x 10<sup>4</sup><br>
1 ≤ Q ≤ 10<sup>4</sup><br>
1 ≤ |li[i]|, |x| ≤ 100


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Tree` `Trie` `Data Structures` `Algorithms` `Advanced Data Structure`
- **Company Tags:** `None`
