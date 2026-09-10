class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for _ in range(len(nums) + 1)]
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for num in freq:
            count[freq[num]].append(num)

        res = []
        i = len(nums)
            
        while len(res) != k:
            if len(count[i]) != 0:
                for n in count[i]:
                    res.append(n)
            i -= 1

        return res

        