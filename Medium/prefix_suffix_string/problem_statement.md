<h1 align="center">Prefix Suffix String</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 54.18%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 24K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two Lists of <b>strings s1 </b>and <b>s2</b>, you have to count the number of strings in <b>s2 </b>which is either a <b>suffix </b>or <b>prefix </b>of at least one string of <b>s1</b>.

<b>Example 1:</b>

<pre><b>Input:</b>
s1 = ["cat", "catanddog", "lion"]
s2 = ["cat", "dog", "rat"]
<b>Output: 
2</b>
<b>Explanation:</b> 
String "cat" of s2 is prefix of "catand<b>dog</b>"
& string "dog" of s2 is suffix of "catand<b>dog</b>" 
</pre>

<b>Example 2:</b>

<pre><b>Input:</b> 
s1 = ["jrjiml", "tchetn", "ucrhye", "ynayhy", 
       "cuhffd", "cvgpoiu", "znyadv"]
s2 = ["jr", "ml", "cvgpoi", "gpoiu", "wnmkmluc", 
      "geheqe", "uglxagyl", "uyxdroj"] 
<b>Output: 
4
Explanation:</b> 
String "jr" of s2 is prefix of "<b>jr</b>jiml", 
"ml" of s2 is suffix of "jrji<b>ml</b>", 
"cvgpoi" of s2 is prefix of "<b>cvgpoi</b>u" &
"gpoiu" of s2 is suffix of "cv<b>gpoiu</b>"<b>
</b></pre>

<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function prefixSuffixString(), which takes 2 strings s1 and s2 as input and returns an integer value as the number of strings in s2 which is a prefix or suffix in s1.

<b>Expected Time Complexity</b>: O(max(len(s1) , len(s2) ))<br>
<b>Expected Space Complexity</b>: O(1)

<b>Constraints:</b><br>
   1 <= s1,s2 < 5 * 10^3<br>
   5 <= len(s1[i]), len(s2[i]) < 25<br>


<hr>

### Tags
- **Topic Tags:** `Strings` `Trie` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Counting Common Prefix Suffix Strings In Two Lists](https://www.geeksforgeeks.org/counting-common-prefix-suffix-strings-in-two-lists/)
