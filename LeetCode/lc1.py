class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                # print([buff_dict[nums[i]], i])
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 18
    Solution().twoSum(nums, target)