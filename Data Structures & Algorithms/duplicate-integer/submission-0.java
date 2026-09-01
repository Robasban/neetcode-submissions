class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> bob = new HashSet<Integer>();
        for(int n : nums){
            if(bob.contains(n)) return true;
            bob.add(n);
        }
        return false;
    }
}
