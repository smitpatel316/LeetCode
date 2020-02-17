class Solution {
    public int singleNumber(int[] nums) {
        ArrayList not_duplicate = new ArrayList();
        for(int i = 0; i<nums.length; i++){
            if(!(not_duplicate.contains(nums[i]))){
                not_duplicate.add(nums[i]);
            }
            else{
                not_duplicate.remove(((Object) nums[i]));
            }
        }
        return (int) not_duplicate.get(0);
    }
}