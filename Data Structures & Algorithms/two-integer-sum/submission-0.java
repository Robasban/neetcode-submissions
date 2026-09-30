class Solution {
    public int[] twoSum(int[] nums, int target) {
        int low = 0, high = nums.length-1;
        int[] bob = new int[2];
        while(true){
            if(nums[low]+nums[high]==target){
                bob[0]=low;
                bob[1]=high;
                return bob;
            } 
            if(nums[low]+nums[high]>target) high--;
            if(nums[low]+nums[high]<target) low++;
        }
    }
}
