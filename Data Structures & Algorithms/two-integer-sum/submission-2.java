class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> bob = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            if(bob.containsKey(target-nums[i])) return new int[]{bob.get(target-nums[i]),i};
            bob.put(nums[i],i);
        }
        return new int[]{};
    }
}
