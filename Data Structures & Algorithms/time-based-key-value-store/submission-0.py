class TimeMap:

    def __init__(self):
        self.time_dict={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_dict:
            self.time_dict[key]=[]
        self.time_dict[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, all_vals= "",self.time_dict.get(key,[])
        if len(all_vals)==0:
            return res
        left, right= 0, len(all_vals)-1
        while left<=right:
            mid= left+(right-left)//2
            if all_vals[mid][1]<=timestamp:
                res= all_vals[mid][0]
                left=mid+1
            else:
                right=mid-1
        return res
