<h1 align="center">Serialize and deserialize a binary tree</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.67%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 100K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 45m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Serialization is to store a tree in an array so that it can be later restored and deserialization is reading tree back from the array. Complete the functions

- <b>serialize() :</b> stores the tree into an array <b>a</b> and returns the array.
- <b>deSerialize() :</b> deserializes the array to the tree and returns the root of the tree.
<b>Note: </b>Multiple nodes can have the same data and the node values are <b>always</b> <b>positive integers</b>. Your code will be correct if the tree returned by <b>deSerialize(serialize(input_tree))</b> is same as the input tree. Driver code will print the in-order traversal of the tree returned by deSerialize(serialize(input_tree)).

<b>Examples :</b>

<pre><b>Input: </b>root = [1, 2, 3]
      
<b>Output: </b>[2, 1, 3]
</pre>

<pre><b>Input:</b> root = [10, 20, 30, 40, 60, N, N]
      
<b>Output: </b>[40, 20, 60, 10, 30]</pre>

<b>Constraints:</b><br>1 <= Number of nodes <= 10<sup>4</sup><br>1 <= Data of a node <= 10<sup>9</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `Paytm` `Flipkart` `Accolite` `Amazon` `Microsoft` `MAQ Software` `Adobe` `Linkedin` `Quikr` `Yahoo` `InMobi`

### Related Articles
- [Serialize Deserialize Binary Tree](https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/)

### Related Interview Experiences
- [Maq Software Interview Experience Set 16 On Campus Fteinternship](https://www.geeksforgeeks.org/maq-software-interview-experience-set-16-on-campus-fteinternship/)
- [Accolite Interview Experience Set 11 On Campus](https://www.geeksforgeeks.org/accolite-interview-experience-set-11-on-campus/)
- [Paytm Interview Experience Set 10 Experienced](https://www.geeksforgeeks.org/paytm-interview-experience-set-10-experienced/)
- [Microsoft Interview Experience Set 157 Campus](httpss://www.geeksforgeeks.org/microsoft-interview-experience-set-157-campus/)
- [Flipkart Interview Set 8 Sde 1](https://www.geeksforgeeks.org/flipkart-interview-set-8-sde-1/)
