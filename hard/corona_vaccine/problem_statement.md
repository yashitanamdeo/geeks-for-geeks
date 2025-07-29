<h1 align="center">Corona Vaccine</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 61.92%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 8K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Geek has successfully developed an effective vaccine for the Coronavirus and aims to ensure that every house in Geek Land has access to it. The houses in Geek Land are structured as a <b>binary tree</b>, where each node represents a house, and the edges denote direct connections between houses.

Each house that receives a <b>vaccine kit</b> can provide coverage to:

- Itself
- Its direct parent house (if it exists)
- Its immediate child houses (if any exist)
Your task is to determine the minimum number of houses that must be supplied with a vaccine kit to ensure that every house is covered.

<b>Examples:</b>

<pre><b>Input:</b> root = [1, 2, 3, N, N, N, 4, N, 5, N, 6]<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/886892/Web/Other/blobid0_1739010580.png" alt="" title="" width="400" height="356"/>

<b>Output: </b>2
<b>Explanation: </b>The vaccine kits should be supplied to house numbers 1 and 5.
</pre>

<pre><b>Input: </b>root = [1, 2, 3]<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/886892/Web/Other/blobid1_1739010580.png" alt="" title="" width="337" height="308"/>
<b>Output: </b>1
<b>Explanation: </b>The vaccine kits should be supplied to house number 1.</pre>

<b>Constraints:</b><br>1 ≤ number of nodes ≤ 10<sup>5</sup>

1 ≤  node->data  ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Minimize Supply Of Corona Vaccines For N Houses If A Vaccine Is Sufficient For Immediate Neighbours](https://www.geeksforgeeks.org/minimize-supply-of-corona-vaccines-for-n-houses-if-a-vaccine-is-sufficient-for-immediate-neighbours/)
