class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        i = 0
        while i < len(nums):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                # print(f"{i}, {j}, {k}, {nums}")
                if nums[i] + nums[j] + nums[k] == 0:
                    # print("boom")
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1 
                    while k > k and nums[k] == nums[k + 1]:
                        k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        return triplets