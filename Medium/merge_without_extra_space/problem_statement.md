<h1 align="center">Merge Without Extra Space</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 32.01%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 306K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two sorted arrays <b>a[]</b> and <b>b[] </b>of size <b>n </b>and <b>m </b>respectively, the task is to merge them in sorted order without using any <b>extra space</b>. Modify <b>a[]</b> so that it contains the first <b>n</b> elements and modify <b>b[]</b> so that it contains the last <b>m</b> elements.

<b>Examples:</b>

<pre><b>Input</b>: a[] = [2, 4, 7, 10], b[] = [2, 3]
<b>Output</b>:<br>[2, 2, 3, 4]<br>[7, 10]
<b>Explanation</b>: After merging the two non-decreasing arrays, we get, 2 2 3 4 7 10</pre>

<pre><b>Input</b>: a[] = [1, 5, 9, 10, 15, 20], b[] = [2, 3, 8, 13]
<b>Output</b>:<br>[1, 2, 3, 5, 8, 9]<br>[10, 13, 15, 20]
<b>Explanation</b>: After merging two sorted arrays we get 1 2 3 5 8 9 10 13 15 20.
</pre>

<pre><b>Input</b>: a[] = [0, 1], b[] = [2, 3]
<b>Output</b>:<br>[0, 1]<br>[2, 3]
<b>Explanation</b>: After merging two sorted arrays we get 0 1 2 3.</pre>

<b>Constraints:</b><br>1 ≤ a.size(), b.size() ≤ 10<sup>5</sup><br>0 ≤ a[i], b[i] ≤ 10<sup>7</sup>

## Expected Complexities
- Time Complexity: O(nlogn + mlogm)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Sorting` `Algorithms` `Arrays`
- **Company Tags:** `Zoho` `Microsoft` `Snapdeal` `Goldman Sachs` `Adobe` `Linkedin` `Amdocs` `Brocade` `Juniper Networks` `Quikr` `Synopsys`

### Related Articles
- [Merge Two Sorted Arrays O1 Extra Space](https://www.geeksforgeeks.org/merge-two-sorted-arrays-o1-extra-space/)
- [Merge Two Sorted Arrays](https://www.geeksforgeeks.org/merge-two-sorted-arrays/)

### Related Interview Experiences
- [Adobe Interview Experience Shecodes 2020 Product Intern](https://www.geeksforgeeks.org/adobe-interview-experience-shecodes-2020-product-intern/)
