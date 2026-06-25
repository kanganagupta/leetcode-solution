class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        queue<int> q;
        int c =0;
        for(int x:nums){
            if(x==0)c++;
            else q.push(x);
        }
        while(c--){
            q.push(0);
        }
        for(int i=0;i<nums.size();i++){
            nums[i]=q.front();
            q.pop();
        }
    }
};
