class Solution {
public:
    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();

        // {end, start, weight, original index}
        vector<vector<int>> arr(n);

        for (int i = 0; i < n; i++) {
            arr[i] = {
                intervals[i][1],
                intervals[i][0],
                intervals[i][2],
                i
            };
        }

        sort(arr.begin(), arr.end());

        // dp[i][k] = maximum weight using first i intervals
        // while selecting at most k intervals.
        vector<vector<long long>> dp(
            n + 1,
            vector<long long>(5, 0)
        );

        // Store selected original indices
        vector<vector<vector<int>>> chosen(
            n + 1,
            vector<vector<int>>(5)
        );

        for (int i = 1; i <= n; i++) {

            int end = arr[i - 1][0];
            int start = arr[i - 1][1];
            int weight = arr[i - 1][2];
            int originalIndex = arr[i - 1][3];

            // Find last interval whose end < current start
            int left = 0;
            int right = i - 2;
            int prev = -1;

            while (left <= right) {
                int mid = left + (right - left) / 2;

                if (arr[mid][0] < start) {
                    prev = mid;
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }

            int prevIndex = prev + 1;

            for (int k = 1; k <= 4; k++) {

                // Option 1: Don't take current interval
                dp[i][k] = dp[i - 1][k];
                chosen[i][k] = chosen[i - 1][k];

                // Option 2: Take current interval
                long long take = weight + dp[prevIndex][k - 1];

                vector<int> candidate = chosen[prevIndex][k - 1];
                candidate.push_back(originalIndex);

                sort(candidate.begin(), candidate.end());

                // Compare weight first.
                // If equal, choose lexicographically smaller indices.
                if (take > dp[i][k] ||
                    (take == dp[i][k] &&
                     candidate < chosen[i][k])) {

                    dp[i][k] = take;
                    chosen[i][k] = candidate;
                }
            }
        }

        // We can select at most 4 intervals.
        vector<int> answer = chosen[n][4];

        sort(answer.begin(), answer.end());

        return answer;
    }
};