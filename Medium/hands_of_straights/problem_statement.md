<h1 align="center">Hands of Straights</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 57.58%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 25K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Alice has some cards, each card has one number written on it. She wants to rearrange the cards into groups so that each group is of size <b>groupSize</b>, and consists of <b>groupSize </b>consecutive cards.<br>Given an integer array <b>hand</b> of size <b>N</b> where <b>hand [ i ]</b> is the value written on the <b>i<sup>th</sup></b> card and an integer <b>groupSize</b>, return <b>true</b> if she can rearrange the cards, or <b>false</b> otherwise.

<b>Example 1:</b>

<b>Input:</b><br>N = 9<br>groupSize = 3<br>hand[ ] = {1, 2, 3, 6, 2, 3, 4, 7, 8}<br><b>Output: </b>true<br><b>Explanation:</b> <br>Alice's hand can be rearranged as {1, 2, 3} , {2, 3, 4}, {6, 7, 8}. There are three groups with size 3. Each group has 3 consecutive cards.
<b>Example 2:</b>

<b>Input:</b><br>N = 5<br>groupSize = 2<br>hand[ ] = {1, 2, 3, 4, 5}<br><b>Output: </b>false<br><b>Explanation:</b> <br>Alice's hand cannot be rearranged into groups of 2. Since there are 5 cards and 5 cards cannot be divided into groups of 2.
<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>isStraightHand()</b> which takes the interger <b>N</b>, integer <b>groupSize</b> and an integer array <b>hand </b>as parameters and returns the true if specified arrangement is possible.

<b>Expected Time Complexity:</b> O(Nlog(N))<br><b>Expected Auxiliary Space:</b> O(N)

<b>Constraints:</b><br>1 ≤ N ≤ 10<sup>5</sup><br>1 ≤ groupSize ≤ N<br>0 ≤ hand<sub>i</sub> ≤ 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Hash` `Greedy` `Sorting` `Data Structures` `Algorithms`
- **Company Tags:** `None`
