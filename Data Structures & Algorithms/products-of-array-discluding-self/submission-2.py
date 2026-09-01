class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(0, len(nums) - 1):
            postfix[len(nums) - 2 - i] = postfix[len(nums) - 1 - i] * nums[len(nums) - 1 - i]
        product = [1] * len(nums)
        for i in range(len(product)):
            product[i] = prefix[i] * postfix[i]
        return product
