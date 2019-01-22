# Runtime: 88 ms, faster than 5.91%    合并两个有序数组
# 思路：把数组2替换掉数组1里的0，然后排序

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        for i in range(len(nums1)):
            for j in range(len(nums1)-1):
                if nums1[i] < nums1[j]:
                    temp = nums1[i]
                    nums1[i] = nums1[j]
                    nums1[j] = temp

if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    Solution().merge(nums1,m,nums2,n)