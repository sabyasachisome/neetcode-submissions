class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def check_num(arr, left, right, target):
            while left<=right:
                mid= left+ (right-left)//2
                if target==arr[mid]:
                    return True
                if target>arr[mid]:
                    left=mid+1
                else:
                    right=mid-1
            return -1
        
        for arr in matrix:
            val= check_num(arr, 0, len(arr)-1, target)
            if val==True:
                return val
        return False
