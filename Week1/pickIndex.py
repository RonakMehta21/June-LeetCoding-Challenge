class Solution:

    def __init__(self, w: List[int]):
        self.sums = []
        t = 0
        for weight in w:
            t+=weight
            self.sums.append(t)
        self.total = t

    def pickIndex(self) -> int:
        target = self.total * random.random()
        low, high = 0, len(self.sums)
        while low<high:
            mid = low + (high-low)//2
            if target > self.sums[mid]:
                low = mid+1
            else:
                high = mid
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
