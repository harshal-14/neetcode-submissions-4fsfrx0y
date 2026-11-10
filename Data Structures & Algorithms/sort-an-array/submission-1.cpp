class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        int n = size(nums);
        
        for(int pass = 0; pass < n -1; ++pass){
            bool swapped = false;
            for(int i =0; i + 1< n - pass; ++i){
                if(nums[i] > nums[i+1]){
                    int temp = nums[i];
                    nums[i] = nums[i+1];
                    nums[i+1] = temp;
                    swapped = true;
                }
            
            }
            if (!swapped) break;
        } 
        return nums;
    }

};