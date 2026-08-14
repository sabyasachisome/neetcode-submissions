class Solution:
    def trap(self, height: List[int]) -> int:
        # n= len(height)

        # leftmax=[0]*n
        # rightmax=[0]*n

        # leftmax[0]=height[0]

        # for i in range(1,n):
        #     leftmax[i]= max(leftmax[i-1], height[i])
        
        # rightmax[n-1]= height[n-1]
        # for i in range(n-2,-1,-1):
        #     rightmax[i]= max(rightmax[i+1], height[i])
        
        # total_water=0
        # for i in range(n):
        #     total_water+=(min(leftmax[i],rightmax[i])-height[i])
        
        # return total_water
        left_max, right_max= [0]*len(height),[0]*len(height)
        left=0
        left_max[0]= height[0]
        for idx in range(1, len(height)):
            left_max[idx]= max(left_max[idx-1], height[idx])
        
        right_max[-1]= height[-1]
        for idx in range(len(height)-2, -1,-1):
            right_max[idx]= max(right_max[idx+1], height[idx])
        
        # print(left_max, right_max)

        total_water=0
        for idx in range(len(height)):
            total_water+= (min(left_max[idx], right_max[idx])- height[idx])
        
        return total_water
