class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        occurrences = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n in count:
            occurrences[count[n]].append(n)

        for i in range(len(occurrences) - 1, -1, -1):
            for j in range(len(occurrences[i])):
                res.append(occurrences[i][j])
                if len(res) == k:
                    return res

