<h1 align="center">Implement Trie</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 65.68%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 76K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Implement <b>Trie</b> class and complete <b>insert(),</b> <b>search() </b>and<b> isPrefix() </b>function for the following queries :

- Type 1 : (1, word), calls insert(word) function and insert word in the Trie
- Type 2 : (2, word), calls search(word) function and check whether word exists in Trie or not.
- Type 3 : (3, word), calls isPrefix(word) function and check whether word exists as a prefix of any string in Trie or not.
<b>Examples :</b>

<pre><b>Input: </b>query[][] = [[1, "abcd"], [1, "abc"], [1, "bcd"], [2, "bc"], [3, "bc"], [2, "abc"]]<br><b>Output: </b>[false, true, true]<br><b>Explanation: </b>string "bc" does not exist in the trie, "bc" exists as prefix of the word "bcd" in the trie, and "abc" also exists in the trie.</pre>

<pre><b>Input: </b>query[][] = [[1, "gfg"], [1, "geeks"], [3, "fg"], [3, "geek"], [2, "for"]]<br><b>Output:</b> [false, true, false]<br><b>Explanation:</b> The string "for" is not present in the trie, "fg" is not a valid prefix, while "geek" is a valid prefix of the word "geeks" in the trie.</pre>

<b>Constraints:<br></b>1 ≤ query.size() ≤ 10<sup>4<br></sup>1 ≤ word.size() ≤ 10<sup>3</sup>


<hr>

### Tags
- **Topic Tags:** `Trie` `Design-Pattern` `Advanced Data Structure`
- **Company Tags:** `Accolite` `Amazon` `Microsoft` `D-E-Shaw` `FactSet`

### Related Articles
- [Introduction To Trie Data Structure And Algorithm Tutorials](https://www.geeksforgeeks.org/introduction-to-trie-data-structure-and-algorithm-tutorials/)
- [Trie Insert And Search](https://www.geeksforgeeks.org/trie-insert-and-search/)
