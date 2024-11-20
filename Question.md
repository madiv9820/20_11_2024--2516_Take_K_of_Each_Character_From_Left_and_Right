# [2516. Take K of Each Character From Left and Right](https://leetcode.com/problems/take-k-of-each-character-from-left-and-right)

__Type:__ Medium <br>
__Topics:__ Hash Table, String, Sliding Window <br>
<hr>

You are given a string `s` consisting of the characters `'a'`, `'b'`, and `'c'` and a non-negative integer `k`. Each minute, you may take either the __leftmost__ character of `s`, or the __rightmost__ character of `s`.

Return _the __minimum__ number of minutes needed for you to take __at least___ `k` _of each character, or return_ `-1` _if it is not possible to take_ `k` _of each character_.
<hr>

### Examples:

- **Example 1:** <br>
**Input:** s = "aabaaaacaabc", k = 2 <br>
**Output:** 8 <br>
**Explanation:** <br>
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character. <br>
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters. <br>
A total of 3 + 5 = 8 minutes is needed. <br>
It can be proven that 8 is the minimum number of minutes needed.

- **Example 2:** <br>
**Input:** s = "a", k = 1 <br>
**Output:** -1 <br>
**Explanation:** It is not possible to take one 'b' or 'c' so return -1.
<hr>

### Constraints:
- <code>1 <= s.length <= 10<sup>5</sup></code>
- `s` consists of only the letters `'a'`, `'b'`, and `'c'`.
- `0 <= k <= s.length`
<hr>

### Hints:
- Start by counting the frequency of each character and checking if it is possible.
- If you take x characters from the left side, what is the minimum number of characters you need to take from the right side? Find this for all values of x in the range 0 ≤ x ≤ s.length.
- Use a two-pointers approach to avoid computing the same information multiple times.