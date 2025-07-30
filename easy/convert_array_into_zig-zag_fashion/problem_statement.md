<h1 align="center">Convert array into Zig-Zag fashion</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 58.28%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 152K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr</b> of <b>distinct </b>elements, the task is to rearrange the elements of the array in a <b>zig-zag fashion</b> so that the converted array should be in the below form: 


arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n]. 


Note: Modify the given arr[] only,<b> </b>If your transformation is correct, the output will be "<b>true"</b> else the output will be <b>"false"</b>. 

<b>Examples</b>

<pre><b>Input: </b>arr[] = [4, 3, 7, 8, 6, 2, 1]
<b>Output: </b>true
<b>Explanation:</b>  After modification the array will look like 3 < 7 > 4 < 8 > 2 < 6 > 1, the checker in the driver code will produce 1.</pre>

<pre><b>Input: </b>arr[] = [4, 7, 3, 8, 2]
<b>Output:</b> true
<b>Explanation: </b>After<b> </b>modification the array will look like 4 < 7 > 3 < 8 > 2 hence output will be 1.<br></pre>

<pre><b>Input: </b>arr[] = [2, 8, 1, 7, 5, 9]
<b>Output:</b> true</pre>

<b>Constraints:</b><br>1 <= arr.size() <= 10<sup>6</sup><br>0 <= arr<sub>i</sub> <= 10<sup>8</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures`
- **Company Tags:** `Paytm` `Amazon` `Adobe`

### Related Articles
- [Convert Array Into Zig Zag Fashion](https://www.geeksforgeeks.org/convert-array-into-zig-zag-fashion/)

### Related Interview Experiences
- [One97paytm Interview Experience](https://www.geeksforgeeks.org/one97paytm-interview-experience/)
- [Adobe Interview Experience On Campus For Internship](https://www.geeksforgeeks.org/adobe-interview-experience-on-campus-for-internship/)
