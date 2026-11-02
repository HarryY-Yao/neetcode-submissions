class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if ((len(self.small) - len(self.large) > 1) or 
        (len(self.large) and len(self.small) and self.small[0] * -1 > self.large[0])):
            temp = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, temp)

        if len(self.large) - len(self.small) > 1:
            temp = heapq.heappop(self.large) * -1
            heapq.heappush(self.small, temp)

    def findMedian(self) -> float:
        if len(self.small) == 0 and len(self.large) == 0:
            return None

        if (len(self.small) + len(self.large)) % 2 == 0:
            return (-self.small[0] + self.large[0]) / 2
        
        else:
            if len(self.small) > len(self.large):
                return -self.small[0]
            else:
                return self.large[0]
        
