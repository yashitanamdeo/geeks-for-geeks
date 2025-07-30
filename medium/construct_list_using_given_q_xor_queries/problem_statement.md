<h1 align="center">Construct list using given q XOR queries</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.86%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 37K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a list <b>s</b> that initially contains only a single value <b>0</b>. There will be <b>q</b> queries of the following types:

- <b>0 x</b>: Insert x in the list
- <b>1 x</b>: For every element a in s, replace it with a ^ x. ('^' denotes the bitwise XOR operator)
Return the sorted list after performing the given <b>q</b> queries.

<b>Example 1:</b>

<pre><b>Input:
</b>q = 5
queries[] = {{0, 6}, {0, 3}, {0, 2}, {1, 4}, {1, 5}}
<b>Output:
</b>1 2 3 7
<b>Explanation:</b>
[0] (initial value)
[0 6] (add 6 to list)
[0 6 3] (add 3 to list)
[0 6 3 2] (add 2 to list)
[4 2 7 6] (XOR each element by 4)
[1 7 2 3] (XOR each element by 5)
The sorted list after performing all the queries is [1 2 3 7]. 
</pre>

<b>Example 2:</b>
<pre><b>Input:
</b>q = 3
queries[] = {{0, 2}, {1, 3}, {0, 5}} 
<b>Output :</b>
1 3 5
<b>Explanation:</b>
[0] (initial value)
[0 2] (add 2 to list)
[3 1] (XOR each element by 3)
[3 1 5] (add 5 to list)
The sorted list after performing all the queries is [1 3 5].
</pre>

<br><b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>constructList()</b> which takes an integer <b>q</b> the number of queries and <b>queries[]</b> a list of lists of length 2 denoting the queries as input parameters and returns the final constructed list.

<br><b>Expected Time Complexity:</b> O(q*log(q))<br><b>Expected Auxiliary Space:</b> O(l), where l is only used for output-specific requirements.

<br><b>Constraints:</b><br>1 ≤ q ≤ 10<sup>5</sup>

0 ≤ x ≤10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Bit Magic` `Data Structures`
- **Company Tags:** `Amazon` `Google`

### Related Articles
- [Construct A List Using The Given Q Xor Queries](https://www.geeksforgeeks.org/construct-a-list-using-the-given-q-xor-queries/)

### Related Interview Experiences
- [Google Online Challenge 2020](https://www.geeksforgeeks.org/google-online-challenge-2020/)
