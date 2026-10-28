class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):

            for j in range(i):

                if nums[i] + nums[j] == target:

                    index1 = j
                    index2 = i

                    list1 = [index1, index2]

                    return list1