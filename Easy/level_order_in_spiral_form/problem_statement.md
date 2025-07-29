<h1 align="center">Level Order in spiral form</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 36.43%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 232K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary tree and the task is to find the spiral order traversal of the tree and return the list containing the elements.<br><b>Spiral order Traversal mean:</b> Starting from level 0 for root node, for all the even levels we print the node's value from right to left and for all the odd levels we print the node's value from left to right. <br>For below tree, function should return [1, 2, 3, 4, 5, 6, 7]

<b> <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700201/Web/Other/blobid0_1746530348.webp" alt="" title="" width="244" height="218"/></b>

<b>Examples:</b>

<pre><b>Input: </b>root = [1, 3, 2]<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700201/Web/Other/blobid2_1746530526.webp" alt="" title="" width="167" height="135"/> <br><b>Output: </b>[1, 3, 2]<br><b>Explanation</b>: Start with root (1), print level 0 (right to left), then level 1 (left to right).</pre>

<pre><b>Input: </b>root = [10, 20, 30, 40, 60]<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700201/Web/Other/blobid3_1746530612.webp" alt="" title="" width="197" height="210"/><br><b>Output: </b>[10, 20, 30, 60, 40]<br><b>Explanation</b>: Start with root (10), print level 0 (right to left), level 1 (left to right), and continue alternating.</pre>

<pre><b>Input: </b>root = [1, 2, N, 4]<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700201/Web/Other/blobid0_1746530910.webp" alt="" title="" width="174" height="185"/>  <br><b>Output: </b>[1, 2, 4]<br><b>Explanation</b>: Start with root (1), then level 1 (left to right), then level 2 (right to left).</pre>

<b>Constraints:</b><br>1 <= number of nodes <= 10<sup>5</sup><br>0 <= node->data <= 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Recursion` `Stack` `Tree` `Data Structures` `Algorithms`
- **Company Tags:** `Flipkart` `Morgan Stanley` `Accolite` `Amazon` `Microsoft` `Hike` `Housing.com` `MakeMyTrip` `Ola Cabs` `Payu` `Teradata` `Walmart` `Adobe`

### Related Articles
- [Level Order Traversal In Spiral Form](https://www.geeksforgeeks.org/level-order-traversal-in-spiral-form/)

### Related Interview Experiences
- [Flipkart Interview Experience Set 24](https://www.geeksforgeeks.org/flipkart-interview-experience-set-24/)
- [Hike Interview Experience Set 5](https://www.geeksforgeeks.org/hike-interview-experience-set-5/)
- [Adobe Interview Experience Set 47](https://www.geeksforgeeks.org/adobe-interview-experience-set-47/)
- [Amazon Interview Experience Set 357 1 5 Years Experienced](https://www.geeksforgeeks.org/amazon-interview-experience-set-357-1-5-years-experienced/)
- [Ola Interview Experience Set 12](https://www.geeksforgeeks.org/ola-interview-experience-set-12/)
- [Accolite Interview Experience Set 13 On Campus For Internship And Fte](https://www.geeksforgeeks.org/accolite-interview-experience-set-13-on-campus-for-internship-and-fte/)
- [Make My Trip Interview Experience On Campus](https://www.geeksforgeeks.org/make-my-trip-interview-experience-on-campus/)
