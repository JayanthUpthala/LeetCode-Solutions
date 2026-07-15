class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        lmax = height[0]
        rmax = height[-1]
        res = 0
        
        rheight = [0]*length
        rheight[-1] = rmax
        for i in range(length-1, -1, -1):
            rmax = max(rmax, height[i])
            rheight[i] = rmax
        
        
        for i in range(length-1):
            lmax = max(lmax, height[i])
            hei = min(lmax, rheight[i])
            ahei = hei - height[i]
            res += ahei
        return res