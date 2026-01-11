#Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # frequency count (bruteforce style)
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # sort based on frequency (descending)
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # take top k based on rank (index)
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])

        return result


#Products of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # LEFT pass
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]

        # RIGHT pass
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res

#Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if n - 1 not in num_set:   # start of sequence
                length = 1
                while n + length in num_set:
                    length += 1
                longest = max(longest, length)

        return longest
