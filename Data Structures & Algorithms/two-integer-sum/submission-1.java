class Solution {
    public int[] twoSum(int[] nums, int target) {
        int low = 0, high = nums.length-1;
        int[] bob = new int[2];
        Arrays.sort(nums);
        while(true){
            if(nums[low]+nums[high]==target){
                return new int[]{low, high};
            } 
            if(nums[low]+nums[high]>target) high--;
            if(nums[low]+nums[high]<target) low++;
        }
    }
}
