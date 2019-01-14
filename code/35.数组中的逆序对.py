'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。
并将P对1000000007取模的结果输出。 即输出P%1000000007
'''
# -*- coding:utf-8 -*-
class Solution:
    def InversePairs1(self, data):
        length = len(data)
        count = 0
        for i in range(length):
            for j in range(i+1,length):
                if data[i]>data[j]:
                    count+=1
        return count #O(n**2)
    def InversePairs(self,data):
        data,count = self.merge_sort(data)
        return count
    def merge_sort(self,array):
        if len(array) == 1:
            return array,0
        mid = len(array)//2
        left,count1 = self.merge_sort(array[:mid])
        right,count2 = self.merge_sort(array[mid:])
        return self.merge(left,right,count1+count2)

    def merge(self,left,right,count):
        i,j = 0,0
        result = []
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                count+=(len(left)-i)
                result.append(right[j])
                j+=1
        result.extend(left[i:])
        result.extend(right[j:])
        return result,count

def test_function():
    solution = Solution()
    data = [1,2,9,0]
    result = solution.InversePairs1(data)
    print(result)
    print(solution.InversePairs(data))


if __name__ == '__main__':
    test_function()