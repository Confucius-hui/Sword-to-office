'''
输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        n = len(tinput)
        if n < k:
            return []
        if n == 0:
            return []
        if k == 0:
            return []
        self.QuickSort(tinput,0,n-1)
        return tinput[:k]
    def QuickSort(self,nums,start,end):
        if start<end:
            i = start
            j = end
            target = nums[i]
            while i<j:
                while i<j and nums[j]>=target:
                    j-=1
                nums[i] = nums[j]
                while i<j and nums[i]<=target:
                    i+=1
                nums[j] = nums[i]
            nums[i] = target
            self.QuickSort(nums,start,i-1)
            self.QuickSort(nums,i+1,end)
        return nums
def test_function():
    solution = Solution()
    nums = [4,5,1,6,2,7,3,8]
    solution.QuickSort(nums,0,len(nums)-1)
    print(nums)
if __name__ == '__main__':
    test_function()

