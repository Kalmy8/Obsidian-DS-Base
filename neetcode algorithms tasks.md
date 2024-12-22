## Advices:
- Iterate through the input list as less frequent as possible. You can create an additional collection as a sort of "memory", which will output useful takeaways from a single pass
	- In general, using more helper collections usually saves time
- For search operations, HashMaps is a killer feature
- For sorting by frequencies, lengths, or any other **Real-value random variable** you can use **Bucket Sort** (спортировка подсчетом), which means creating a frequency-counter array + creating a bucket array, there each index represents some frequency ([Problems](https://neetcode.io/problems/top-k-elements-in-list))
	- This is similar to Сортировка Подсчетом
- If you have to store one string with some delimiter, and be able to decode it once back, use a progressive delimiter. Like 1#, 2#, 3# and so on. It's more robust and optimal solution, when using some random sequence/word as a delimiter
