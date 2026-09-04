class Solution {
public:
    int firstStableIndex(vector<int>& nums, int k) {
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            int maxValue = nums[i];
            int minValue = nums[i];

            // Find maximum on the left
            for (int j = 0; j < i; j++) {
                maxValue = max(maxValue, nums[j]);
            }

            // Find minimum on the right
            for (int j = i + 1; j < n; j++) {
                minValue = min(minValue, nums[j]);
            }

            if (maxValue - minValue <= k) {
                return i;
            }
        }

        return -1;
    }
};