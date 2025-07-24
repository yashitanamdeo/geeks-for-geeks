<h1 align="center">Winner of an election</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.75%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 96K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of <i>n </i>names arr of candidates in an election, where each name is a string of lowercase characters. A candidate name in the array represents a vote casted to the candidate. Print the name of the candidate that received the maximum count of votes. If there is a draw between two candidates, then print <i>lexicographically </i>smaller name.

<b>Examples :<br></b>

<pre><b>Input: </b>n = 13
arr[] = {john,johnny,jackie,johnny,john,jackie,jamie,jamie,john,johnny,jamie,johnny,john}
<b>Output: </b>john 4<b>
Explanation: </b>john has 4 votes casted for him, but so does johnny. john is lexicographically smaller, so we print john and the votes he received.</pre>

<pre><b>Input: </b>n = 3
arr[] = {andy,blake,clark}
<b>Output: </b>Andy 1<b>
Explanation: </b>All the candidates get 1 votes each. We print andy as it is lexicographically smaller.
</pre>

<b>Your Task:</b><br>You only need to complete the function <b>winner()</b> that takes an array of strings <b>arr</b>, and length of <b>arr</b> <b>n</b> as parameters and returns an <b>array of string </b>of <b>length 2</b>. First element of the array should be the <b>name </b>of the candidate and second element should be the <b>number of votes </b>that candidate got in <b>string format</b>.

<b>Constraints:</b><br>1 <= n <= 10<sup>5<br></sup>1 <= |arr<sub>i</sub>| <= 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Hash` `Strings` `Data Structures`
- **Company Tags:** `Adobe` `Atlassian`

### Related Articles
- [Find Winner Election Votes Represented Candidate Names](https://www.geeksforgeeks.org/find-winner-election-votes-represented-candidate-names/)

### Related Interview Experiences
- [Atlassian Interview Experience](https://www.geeksforgeeks.org/atlassian-interview-experience/)
