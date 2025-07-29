<h1 align="center">Word Break</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 40.86%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 159K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a string <b>s</b> and a list <b>dictionary[]</b> of words. Your task is to determine whether the string <b>s</b> can be formed by concatenating one or more words from the <b>dictionary[]</b>.

<b>Note</b>: From <b>dictionary[]</b>, any word can be taken any number of times and in any order.

<b>Examples :</b>

<pre><b>Input: </b>s<b> </b>= "ilike", dictionary[] = ["i", "like", "gfg"]<br><b>Output: </b>true
<b>Explanation: </b>s can be breakdown as "i like".
</pre>

<pre><b>Input</b>: s<b> </b>= "ilikegfg", dictionary[] = ["i", "like", "man", "india", "gfg"]
<b>Output: </b>true
<b>Explanation</b>: s can be breakdown as "i like gfg".</pre>

<pre><b>Input</b>: s<b> </b>= "ilikemangoes", dictionary[] = ["i", "like", "man", "india", "gfg"]
<b>Output: </b>false
<b>Explanation</b>: s cannot be formed using dictionary[] words.</pre>

<b>Constraints</b>:<br>1 ≤ s.size() ≤ 3000<br>1 ≤ dictionary.size() ≤ 1000<br>1 ≤ dictionary[i].size() ≤ 100

## Expected Complexities
- Time Complexity: O(n * m)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `Zoho` `Flipkart` `Amazon` `Microsoft` `Hike` `Walmart` `MAQ Software` `Google` `IBM`

### Related Articles
- [Word Break Problem Dp 32](https://www.geeksforgeeks.org/word-break-problem-dp-32/)

### Related Interview Experiences
- [Maq Software Interview Experience Set 9 On Campus For Se 1](https://www.geeksforgeeks.org/maq-software-interview-experience-set-9-on-campus-for-se-1/)
- [Walmart Labs Interview Experience Set 2 On Campus](https://www.geeksforgeeks.org/walmart-labs-interview-experience-set-2-on-campus/)
- [Walmart Lab Interview Experience Set 7 Off Campus](https://www.geeksforgeeks.org/walmart-lab-interview-experience-set-7-off-campus/)
- [Flipkart Interview Set 6](https://www.geeksforgeeks.org/flipkart-interview-set-6/)
- [Flipkart Interview Experience Set 22 For Sde 2](https://www.geeksforgeeks.org/flipkart-interview-experience-set-22-for-sde-2/)
