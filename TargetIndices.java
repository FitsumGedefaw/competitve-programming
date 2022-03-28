class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        List<Integer> result = new ArrayList<Integer>();
            int n = nums.length;
            for(int i = n - 2; i >= 0; i--)
                {
                    for(int j = 0; j <= i; j++)
                        {
                            if(nums[j] > nums[j+1])
                                {
                                    int temp = nums[j];
                                    nums[j] = nums[j+1];
                                    nums[j+1] = temp;
                                }
                        }
                }
            for(int i = 0; i < n; i++)
                {
                    if(nums[i] == target)
                        {
                            result.add(i);
                        }
                }
            return result;  
    }
}
