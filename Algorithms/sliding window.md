---
type: note
status: done
tags: [tech/algorithms]
sources:
-
authors:
-
---

[Site Unreachable](https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4502/)

An approach, suitable for solving "find valid subarray" tasks 
For example:
- Given array [2,3,1,3,5,6,7]
- Find the length of the minimal subarray with sum >= 7
- (Solution is [7])

Description:
- We start creating two pointers like `l = 0` and `r = 0`
- We increment `r`, "adding" values to a subarray
- We incerement `l`, "removing" values from a subarray
	- We do that until `r = len(array)` 