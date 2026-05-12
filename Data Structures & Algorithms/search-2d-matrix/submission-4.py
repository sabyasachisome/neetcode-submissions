class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, m= len(matrix), len(matrix[0])
        r, c= 0, m-1
        while r<l and c>=0:
            if matrix[r][c]>target:
                c-=1
            elif matrix[r][c]<target:
                r+=1
            else:
                return True
        return False
            

        # def check_num(arr, left, right, target):
        #     while left<=right:
        #         mid= left+ (right-left)//2
        #         if target==arr[mid]:
        #             return True
        #         if target>arr[mid]:
        #             left=mid+1
        #         else:
        #             right=mid-1
        #     return -1
        
        # for arr in matrix:
        #     val= check_num(arr, 0, len(arr)-1, target)
        #     if val==True:
        #         return val
        # return False
