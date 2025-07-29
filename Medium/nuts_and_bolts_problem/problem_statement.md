<h1 align="center">Nuts and Bolts Problem</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 59.03%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 78K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a set of <b>n</b> <b>nuts</b> & <b>bolts</b>. There is a one-on-one mapping between nuts and bolts. You have to <b>Match </b>nuts and bolts efficiently. Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means the nut can only be compared with the bolt and the bolt can only be compared with the nut to see which one is bigger/smaller.<br>The elements should follow the following <b>order</b>: <b>{ !,#,$,%,&,*,?,@,^ }</b>

<b>Note</b>: Make all the required changes <b>directly </b>in the given arrays, output will be handled by the driver code.

<b>Examples</b>

<pre><b>Input: </b>n = 5, nuts[] = {@, %, $, #, ^}, bolts[] = {%, @, #, $ ^}
<b>Output:</b> 
# $ % @ ^
# $ % @ ^<br><b>Explanation: </b>As per the order # should come first after that $ then % then @ and ^. </pre>

<pre><b>Input: </b>n = 9, nuts[] = {^, &, %, @, #, *, $, ?, !}, bolts[] = {?, #, @, %, &, *, $ ,^, !}
<b>Output:</b> 
! # $ % & * ? @ ^
! # $ % & * ? @ ^<br><b>Explanation: </b>We'll have to match first ! then  # , $,  %,  &,  *,  @,  ^,  ? as per the required ordering.</pre>

<b>Expected Time Complexity:</b> O(n(logn))<br><b>Expected Auxiliary Space:</b> O(log(n))

<b>Constraints:</b><br>1 <= n <= 9<br>The arrays 'nuts' and 'bolts' can only consist of the following elements: {'@', '#', '$', '%', '^', '&', '?', '*', '!'}.<br>All the elements of arrays 'nuts' and 'bolts' should be unique.


<hr>

### Tags
- **Topic Tags:** `Arrays` `Hash` `Data Structures`
- **Company Tags:** `Amazon` `Hike` `MakeMyTrip` `MAQ Software` `Adobe`

### Related Articles
- [Nuts Bolts Problem Lock Key Problem Using Quick Sort](https://www.geeksforgeeks.org/nuts-bolts-problem-lock-key-problem-using-quick-sort/)

### Related Interview Experiences
- [Maq Software Interview Experience Set 15 On Campus](https://www.geeksforgeeks.org/maq-software-interview-experience-set-15-on-campus/)
- [Makemytrip Interview Experience Set 12](https://www.geeksforgeeks.org/makemytrip-interview-experience-set-12/)
