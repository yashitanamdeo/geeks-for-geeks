<h1 align="center">Smallest window containing all characters</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 30.19%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 184K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two strings <b>s</b> and <b>p</b>. Find the smallest substring in <b>s</b> consisting of all the characters (<b>including duplicates</b>) of the string <b>p</b>. Return empty string in case no such substring is present. <br>If there are multiple such substring of the same length found, return the one with the <b>least starting index</b>.

<b>Examples:</b>

<pre><b>Input: </b>s = "timetopractice", p = "toc"
<b>Output: </b>"toprac"<b>
Explanation: </b>"toprac" is the smallest substring in which "toc" can be found.
</pre>

<pre><b>Input: </b>s = "zoomlazapzo", p = "oza"
<b>Output: </b>"apzo"<b>
Explanation: </b>"apzo" is the smallest substring in which "oza" can be found.<br></pre>

<pre><b>Input: </b>s = "zoom", p = "zooe"
<b>Output:</b> ""<b>
Explanation: </b>No substring is present containing all characters of p.</pre>

<b>Constraints: </b><br>1 ≤ s.length(), p.length() ≤ 10<sup>6<br></sup>s, p consists of lowercase english letters

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `sliding-window` `Hash` `Strings` `Dynamic Programming` `Binary Search`
- **Company Tags:** `Flipkart` `Amazon` `Microsoft` `MakeMyTrip` `Google` `Streamoid Technologies` `Media.net` `Atlassian`

### Related Articles
- [Find The Smallest Window In A String Containing All Characters Of Another String](https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/)

### Related Interview Experiences
- [Makemytrip Interview Experience](https://www.geeksforgeeks.org/makemytrip-interview-experience/)
- [Amazon Interview Experience Set 315](https://www.geeksforgeeks.org/amazon-interview-experience-set-315/)
- [Streamoid Technologies Interview Experience Set 1 For Freshers](https://www.geeksforgeeks.org/streamoid-technologies-interview-experience-set-1-for-freshers/)
- [Makemytrip Interview Experience Set 3](https://www.geeksforgeeks.org/makemytrip-interview-experience-set-3/)
- [Makemytrip Interview Experience Set 2 Campus](https://www.geeksforgeeks.org/makemytrip-interview-experience-set-2-campus/)
- [Directi Interview Experience Set 22 Pool Campus](https://www.geeksforgeeks.org/directi-interview-experience-set-22-pool-campus/)
- [Flipkart Interview Set 5 Off Campus](https://www.geeksforgeeks.org/flipkart-interview-set-5-off-campus/)
- [Flipkart Interview Set 2 For Sde 1](https://www.geeksforgeeks.org/flipkart-interview-set-2-for-sde-1/)
