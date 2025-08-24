<h1 align="center">Minimum days to make M bouquets</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 46.85%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 24K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You have a row of flowers, where each flower blooms after a specific day. The array <b>arr[]</b> represents the blooming schedule: <b>arr[i]</b> is the day the flower at position <b>i</b> will bloom. To create a bouquet, you need to collect <b>k <i>adjacent</i></b> bloomed flowers. Each flower can only be used in one bouquet.

Your goal is to find the <b>minimum </b>number of days required to make exactly <b>m</b> bouquets. If it is not possible to make <b>m</b> bouquets with the given arrangement, return <b>-1</b>.

#### <b>Examples</b>:
<pre><b>Input</b>: m = 3, k = 2, arr[] = [3, 4, 2, 7, 13, 8, 5]
<b>Output</b>: 8
<b>Explanation</b>: We need 3 bouquets and each bouquet should have 2 flowers. After day 8: [x, x, x, x, _, x, x], we can make first bouquet from the first 2 flowers, second bouquet from the next 2 flowers and the third bouquet from the last 2 flowers.</pre>

<pre><b>Input</b>: m = 2, k = 3, arr[] = [5, 5, 5, 5, 10, 5, 5]
<b>Output</b>: 10
<b>Explanation</b>: We need 2 bouquets and each bouquet should have 3 flowers, After day 5: [x, x, x, x, _, x, x], we can make one bouquet of the first three flowers that bloomed, but cannot make another bouquet. After day 10: [x, x, x, x, x, x, x], Now we can make two bouquets, taking 3 adjacent flowers in one bouquet.</pre>

<pre><b>Input: </b>m = 3, k = 2, arr[] = [1, 10, 3, 10, 2]<br><b>Output: </b>-1<br><b>Explanation:</b> As 3 bouquets each having 2 flowers are needed, that means we need 6 flowers. But there are only 5 flowers so it is impossible to get the needed bouquets therefore -1 will be returned.</pre>

<b>Constraints:<br></b>1 ≤ k ≤ arr.size() ≤ 10<sup>5</sup><b><br></b>1 ≤ m ≤ 10<sup>5</sup><br>1 ≤ arr[i] ≤ 10<sup>9</sup>

## Expected Complexities
- Time Complexity: O(n * log(max(arr[i])))
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Binary Search` `Arrays`
- **Company Tags:** `Bloomberg` `Amazon` `Microsoft` `Google` `Flipkart`

### Related Articles
- [Minimum Days To Make M Bouquets](https://www.geeksforgeeks.org/minimum-days-to-make-m-bouquets/)
