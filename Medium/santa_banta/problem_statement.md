<h1 align="center">Santa Banta</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.01%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 29K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Santa is still not married. He approaches a marriage bureau and asks them to hurry the process. The bureau checks the list of eligible girls of size <b>N</b> and hands it over to Santa. Santa being conscious about his marriage is determined to find a girl with <b>maximum</b> connections so that he can gather more information about her. Accordingly, he looks to figure out the <b>maximum </b>number of girls (from the list) who know each other to achieve the above purpose.

In order to finalize the girl, he needs to find the <b>Kth</b> prime. Where k = largest group of girls who know each other. Considering Santa's poor knowledge of Maths, he seeks Banta's help for the answer. Now you, a fan of Santa Banta Jokes, take this prestigious opportunity to solve the problem.

In case no of connections is zero, print "-1". Here the connection between girls is represented by a 2-D array <b>g </b>of dimension M*2, where <b>M</b> is the number of connections.

<b>Note :</b><br>1. Suppose girl "a" knows girl "b" and girl "b" knows girl "c", then girl "a" also knows girl "c". <b>Transitivity</b> holds here.<br>2. Consider 1 as a <b>composite</b> number.<br>3. For precompute function given in the template you just have to complete it and use it wherever required, do not call it again and again, it is already being called by driver function before executing test cases. 

<b>Example 1:</b>

<pre><b>Input :</b> <br>N = 10<br>M = 6<br>g[] = {{1,2},{2,3},{3,4},{4,5},{6,7},{9,10}}
<b>Output :</b> <br>11
<b>Explanation:</b>
Here in this graph there are 4 groups. 
In 1<sup>st</sup> group: (1 -> 2 -> 3 -> 4 -> 5) are 
there. In 2<sup>nd</sup> group: (6 -> 7) are there.
In 3<sup>rd </sup>group: (8) is there.
In 4<sup>th</sup> group: (10 -> 9) are there.
In these 4 group the maximum number of 
value is 5. So, K = 5 and the 5<sup>th</sup> prime number 
is 11. Return 11.
</pre>

<b>Example 2:</b>

<pre><b>Input :</b> <br>N = 2<br>M = 1<br>g[] = {{1, 2}} <b>
Output :</b> <br>3
<b>Explanation:
</b>In this Example there will only be a <br>single group of 2 girls, and hence the <br>value of K is 2, The 2nd prime is 3.
</pre>

<b>Your Task:</b>

This is a function problem. The input is already taken care of by the driver code. You only need to complete the function <b>helpSanta()</b> that takes a number of girls <b>(n)</b>, a number of connections <b>(m),</b> a <b>2-D</b> <b>array </b>of girls connections <b>(g)</b>, and return the Kth prime no if there are no connections then return -1. The driver code takes care of the printing.

<b>Expected Time Complexity:</b> O(N + M).<br><b>Expected Auxiliary Space:</b> O(N + M).

<b>Constraints:<br></b>1 ≤ n ≤ 10<sup>5</sup><br>0 ≤ m ≤ 10<sup>5</sup><br>1 ≤ u, v ≤ n<br>Sum of n+m will not exceed 10<sup>5</sup>.


<hr>

### Tags
- **Topic Tags:** `Arrays` `sieve` `Graph` `Data Structures`
- **Company Tags:** `None`
