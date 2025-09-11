<h1 align="center">Minimum Jumps</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 11.91%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 1M-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array <b>arr[]</b> of non-negative numbers. Each number tells you the <b>maximum number of steps</b> you can jump forward from that position.

For example:

- If <b>arr[i] = 3</b>, you can jump to index <b>i + 1</b>, <b>i + 2</b>, or <b>i + 3</b> from position <b>i</b>.
- If <b>arr[i] = 0</b>, you <b>cannot jump forward</b> from that position.
Your task is to find the <b>minimum number of jumps</b> needed to move from the <b>first</b> position in the array to the <b>last</b> position.

<b>Note:  </b>Return <b>-1</b> if you can't reach the end of the array.

<b>Examples : </b> 

<pre><b>Input: </b>arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
<b>Output:</b> 3 
<b>Explanation: </b>First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last. </pre>

<pre><b>Input: </b>arr = [1, 4, 3, 2, 6, 7]<br><b>Output:</b> 2 
<b>Explanation: </b>First we jump from the 1st to 2nd element and then jump to the last element.</pre>

<pre><b>Input: </b>arr = [0, 10, 20]<br><b>Output:</b> -1
<b>Explanation: </b>We cannot go anywhere from the 1st element.
</pre>

<b>Constraints:</b><br>2 ≤ arr.size() ≤ 10<sup>5<br></sup>0 ≤ arr[i] ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Greedy` `Data Structures` `Algorithms`
- **Company Tags:** `Moonfrog Labs` `Flipkart` `Amazon` `Microsoft` `Housing.com` `Walmart` `Adobe` `Google`

### Related Articles
- [Minimum Number Of Jumps To Reach End Of A Given Array](https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/)

### Related Interview Experiences
- [Adobe Interview Experience Set 36 Off Campus Drive](https://www.geeksforgeeks.org/adobe-interview-experience-set-36-off-campus-drive/)
- [Walmart Lab Interview Experience Set 9 Off Campus](https://www.geeksforgeeks.org/walmart-lab-interview-experience-set-9-off-campus/)
- [Moonfrog Labs Interview Experience Set 4](https://www.geeksforgeeks.org/moonfrog-labs-interview-experience-set-4/)
