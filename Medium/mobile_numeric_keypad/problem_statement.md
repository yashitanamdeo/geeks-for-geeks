<h1 align="center">Mobile numeric keypad</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 32.6%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 69K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There is a standard <b>numeric keypad</b> on a mobile phone. You can press the <b>current button</b> or any button that is directly <b>above</b>, <b>below</b>, to the <b>left</b>, or to the <b>right</b> of it. For example, if you press <b>5</b>, then pressing <b>2</b>, <b>4</b>, <b>6</b>, or <b>8</b> is allowed. However, <b>diagonal movements</b> and pressing the <b>bottom row corner</b> buttons (<b>*</b> and <b>#</b>) are not allowed.<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/704157/Web/Other/blobid0_1718345574.png" alt="" title="" width="190" height="214"/>

Given an integer <b>n</b>, determine how many <b>unique </b>sequences of length <b>n</b> can be formed by pressing buttons on the keypad, starting from any digit.

<b>Examples :</b>

<pre><b>Input</b>: n = 1
<b>Output: </b>10
<b>Explanation</b>: Possible 1-digit numbers follow keypad moves - From 0 → 0, 1 → 1, 2 → 2 and so on, total <b>10</b> valid combinations are possible.</pre>

<pre><b>Input: </b>n = 2
<b>Output: </b>36
<b>Explanation</b>: Possible 2-digit numbers follow keypad moves -<br>From 0 → 00, 08 (2), <br>From 1 → 11, 12, 14 (3),<br>From 3 → 33, 32, 36 (3), and so on,<br>total <b>36</b> valid combinations are possible.</pre>

<b>Constraints:<br></b>1 ≤ n ≤ 15

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms` `Mathematical`
- **Company Tags:** `Flipkart` `Microsoft` `MAQ Software` `Sprinklr`

### Related Articles
- [Mobile Numeric Keypad Problem](https://www.geeksforgeeks.org/mobile-numeric-keypad-problem/)

### Related Interview Experiences
- [Sprinklr Interview Experience Set 2 On Campus](https://www.geeksforgeeks.org/sprinklr-interview-experience-set-2-on-campus/)
- [Microsoft Interview Experience Set 53](https://www.geeksforgeeks.org/microsoft-interview-experience-set-53/)
- [Flipkart Interview Set 11](https://www.geeksforgeeks.org/flipkart-interview-set-11/)
- [Flipkart Interview Experience For Sde 2](https://www.geeksforgeeks.org/flipkart-interview-experience-for-sde-2/)
