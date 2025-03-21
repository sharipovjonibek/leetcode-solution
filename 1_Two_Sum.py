class Solution(object):
    def twoSum(self, nums, target):
        array=[]
        for num in range(0,len(nums)):
            for item in range(0,len(nums)):
                if num==item:
                    continue
                elif nums[num]+nums[item]==target:
                    array.append(num)
                    array.append(item)
                    return sorted(array)
                    