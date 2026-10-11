class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> hashmap;
        // why hashmap because it gives easy O(1) lookup
        for(int i=0; i<nums.size(); i++){
            int diff = target - nums[i];
            if (hashmap.find(diff) != hashmap.end()){
                return {hashmap[diff], i};
            } // this line does 
            hashmap[nums[i]] = i;
        }
    }
};
