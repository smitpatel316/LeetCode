class Solution {
    public void moveZeroes(int[] nums) {
        for(int i = 0, lastNonZeroFound = 0;i<nums.length; i++){
            if(nums[i] != 0){
                int temp = nums[lastNonZeroFound];
                nums[lastNonZeroFound] = nums[i];
                nums[i] = temp;
                lastNonZeroFound++;
            }
        }
    }
}