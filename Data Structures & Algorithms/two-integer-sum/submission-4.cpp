class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> hashmap;
        for(int i = 0; i<nums.size(); i++){
            int difference = target - nums[i];
            if (hashmap.find(difference) != hashmap.end() ){
                return {hashmap[difference], i};
            }
            hashmap[nums[i]] = i;
        }
        }
};
