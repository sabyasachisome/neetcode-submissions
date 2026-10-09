class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min=1,1
        res= max(nums)

        for n in nums:
            # if n==0:
            #     cur_max, cur_min= 1,1
            #     continue
            tmp= cur_max*n
            cur_max= max(cur_max*n, cur_min*n, n)
            cur_min= min(tmp, cur_min*n, n)

            res= max(res, cur_max)
        return res
