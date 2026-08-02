class MedianFinder:

    def __init__(self):
        self.medianFinder=[]

    def addNum(self, num: int) -> None:
        self.medianFinder.append(num)

    def findMedian(self) -> float:
        size= len(self.medianFinder)
        self.medianFinder.sort()
        if size%2==1:
            median_pt= size//2
            return self.medianFinder[median_pt]
        else:
            return (self.medianFinder[size//2]+self.medianFinder[(size//2)-1])/2.0
        