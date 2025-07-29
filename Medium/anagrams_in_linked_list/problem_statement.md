<h1 align="center">Anagrams in Linked List</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 63.42%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 18K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a linked list of characters and a string <b>str</b>. Return all the anagrams of the string present in the given linked list. In case of overlapping anagrams choose the first anagram from left. If there is no anagram in the linked list, return an empty array.

<b>Examples:</b>

<pre><b>Input:</b> Linked list:<b> </b>a -> b -> c -> a -> d -> b -> c -> a, str = bac<b>
Output: </b>[a -> b -> c, b -> c -> a]<b>
Explanation: </b>In the given linked list, there are three anagrams: 
1. <b>a -> b -> c</b> -> a -> d -> b -> c -> a
2. a -> <b>b -> c -> a</b> -> d -> b -> c -> a
3. a -> b -> c -> a -> d -> <b>b -> c -> a<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/714140/Web/Other/blobid0_1723398166.png" alt="" title="" width="401" height="169"/><br></b>But in 1 and 2, a -> b -> c and b -> c-> a are ovelapping.So we take a -> b -> c as it comes first from left.So the output is: [a->b->c,b->c->a]</pre>

<pre><b>Input: </b>Linked list:<b> </b>a -> b -> d -> c -> a, str = bac<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/714140/Web/Other/blobid1_1723398186.png" alt="" title="" width="400" height="50"/><b>
Output: </b>-1<b> 
Explanation: </b>There is no anagrams, so the output is -1</pre>

<b>Expected Time Complexity:</b> O(n)<br><b>Expected Space </b><b>Complexity</b><b>:</b> O(1)

<b>Constraints:</b><br>1 <= size of linked list <= 10<sup>6</sup><sup><br></sup>data of nodes: Only lowercase alphabet<sup><br></sup>


<hr>

### Tags
- **Topic Tags:** `Linked List` `sliding-window`
- **Company Tags:** `None`

### Related Articles
- [Find Anagrams In Linked List](https://www.geeksforgeeks.org/find-anagrams-in-linked-list/)
