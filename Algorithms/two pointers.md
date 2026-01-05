---
type: note
status: done
tags: ['tech/algorithms']
sources:
-
authors:
-
---
#🃏/semantic/algorithms

**Codewords:** two pointers, fast and slow pointers, opposite-end pointers, in-place algorithm, time complexity, space complexity

## Two Pointers Technique

The **Two Pointers** technique is an algorithmic pattern that uses two pointers to iterate through a data structure, typically an array, until they meet or satisfy a certain condition. This approach is highly efficient for problems that involve searching for pairs or subarrays, often reducing the time complexity from O(n^2) to O(n) and using O(1) extra space.

There are two main variations of this technique.

### 1. Pointers at Opposite Ends

In this variation, one pointer starts at the beginning of the array (`left`) and the other starts at the end (`right`). They move towards each other until they meet or cross. This pattern is particularly useful for problems on **sorted arrays**.

**Use Case: Finding a Pair with a Target Sum**

Given a sorted array of integers, find if there is a pair of numbers that add up to a given target.

```python
def find_pair_with_target_sum(arr: list[int], target: int) -> tuple[int, int] | None:
 """
 Finds a pair of numbers in a sorted array that sums up to the target.

 :param arr: A sorted list of integers.
 :param target: The target sum.
 :return: A tuple with the pair of numbers, or None if no such pair is found.
 """
 left = 0
 right = len(arr) - 1

 while left < right:
 current_sum = arr[left] + arr[right]
 if current_sum == target:
 return arr[left], arr[right]
 elif current_sum < target:
 # The sum is too small, we need a larger number. Move the left pointer up.
 left += 1
 else: # current_sum > target
 # The sum is too large, we need a smaller number. Move the right pointer down.
 right -= 1
 
 return None

# Example
my_array = [1, 2, 4, 6, 8, 9, 14, 20]
target_sum = 10
pair = find_pair_with_target_sum(my_array, target_sum)
print(f"Array: {my_array}")
print(f"Target Sum: {target_sum}")
print(f"Found pair: {pair}") # Expected output: (2, 8)
```

**Practice Problem: Two Sum II**

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, *added by one* as an integer array `[index1, index2]` of length 2.

```python
# Toy data for the problem
numbers = [2, 7, 11, 15]
target = 9
# Expected output: [1, 2]

numbers_2 = [2, 3, 4]
target_2 = 6
# Expected output: [1, 3]

numbers_3 = [-1, 0]
target_3 = -1
# Expected output: [1, 2]
```
**Task:**
1. Implement a function that solves this problem using the two-pointers technique.
2. The function should return the 1-based indices of the pair.

---

### 2. Fast and Slow Pointers (Same Direction)

In this pattern, both pointers start at or near the beginning of the data structure. One pointer (the `fast` pointer) moves ahead, while the other (`slow` pointer) moves at a slower pace. The distance between them can be fixed or variable, depending on the problem.

This is very common for cycle detection in linked lists or for problems that deal with processing elements of an array in-place.

**Use Case: Removing Duplicates from a Sorted Array**

Given a sorted array, remove the duplicates in-place such that each element appears only once. The function should return the length of the new array.

```python
def remove_duplicates(arr: list[int]) -> int:
 """
 Removes duplicates from a sorted array in-place.

 :param arr: A sorted list of integers.
 :return: The length of the array after removing duplicates.
 """
 if not arr:
 return 0

 # slow_pointer will track the position for the next unique element.
 slow_pointer = 1 
 
 # fast_pointer will iterate through the array to find unique elements.
 for fast_pointer in range(1, len(arr)):
 if arr[fast_pointer] != arr[fast_pointer - 1]:
 arr[slow_pointer] = arr[fast_pointer]
 slow_pointer += 1
 
 return slow_pointer

# Example
my_array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = remove_duplicates(my_array)
print(f"Array after removing duplicates: {my_array[:new_length]}") # Expected output: [0, 1, 2, 3, 4]
print(f"New length: {new_length}") # Expected output: 5
```

---

**Practice Problem: Squaring a Sorted Array**

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

```python
# Toy data for the problem
nums = [-4, -1, 0, 3, 10]
# Expected output: [0, 1, 9, 16, 100]

nums_2 = [-7, -3, 2, 3, 11]
# Expected output: [4, 9, 9, 49, 121]
```
**Task:**
1. Implement a function that solves this problem efficiently. A naive solution would be to square each element and then sort, which is O(n log n).
2. Can you solve it in O(n) time using two pointers (from opposite ends)? Hint: The largest squared number will be at one of the ends of the original array.

---

**Key Questions:**

2. What are the two primary patterns of the Two Pointers technique?
?
- **Opposite Ends:** One pointer starts at the beginning and the other at the end, and they move towards each other.
- **Fast and Slow:** Both pointers start at the beginning, but one moves faster than the other.
<!--SR:!2025-11-29,1,230-->

3. For which type of problems is the "Opposite Ends" pattern most suitable?
?
- It is most suitable for problems involving **sorted arrays** where you need to find a pair of elements that satisfy a certain condition (e.g., their sum equals a target).
- TODO examples here (trapping rain etc)
<!--SR:!2025-11-29,1,228-->

4. What is a classic example of the "Fast and Slow" pointers pattern?
?
- A classic example is **detecting a cycle in a linked list**. Another common example is removing duplicates from a sorted array in-place.
- TODO examples here (?)
<!--SR:!2025-11-29,1,228-->
