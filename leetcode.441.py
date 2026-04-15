class Solution {
public:
    int arrangeCoins(int n) {

        int l = 0;
        int r = n;
        while (l <= r) {
            long m = l + (r - l) / 2;
            long coins = (m * (m + 1) / 2);
            if (n == coins)
                return m;
            else if (n < coins)
                r = m - 1;
            else
                l = m + 1;
        }
        return r;
    }
};
