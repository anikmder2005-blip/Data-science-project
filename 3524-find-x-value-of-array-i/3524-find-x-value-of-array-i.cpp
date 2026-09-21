class Solution {
public:
    vector<long long> resultArray(vector<int>& nums, int k) {
        vector<long long> ans(k, 0);
        vector<long long> dp(k, 0);

        for (int num : nums) {
            vector<long long> newDp(k, 0);
            int mod = num % k;

            // Start a new subarray containing only num
            newDp[mod] = 1;

            // Extend all previous subarrays
            for (int r = 0; r < k; r++) {
                int newMod = (1LL * r * mod) % k;
                newDp[newMod] += dp[r];
            }

            // Add counts to answer
            for (int r = 0; r < k; r++) {
                ans[r] += newDp[r];
            }

            dp = move(newDp);
        }

        return ans;
    }
};