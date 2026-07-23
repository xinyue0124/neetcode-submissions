class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> res = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int num = nums[i];
            int diff = target - num;
            if(res.containsKey(diff)){
                return new int[]{res.get(diff), i};
            }
            res.put(num, i);
        }
        return new int[]{};
    }
}
