class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        cout << "Starting to check array: ";
        for (int num : nums) {
            cout << num << " ";
        }
        cout << endl;

        for (int num : nums) {
            cout << "Checking number: " << num << endl;
            if (seen.find(num) != seen.end()) {
                cout << "Duplicate found: " << num << endl;
                return true;  // Duplicate found
            }
            seen.insert(num);
            cout << "Set after insertion: ";
            for (int s : seen) {
                cout << s << " ";
            }
            cout << endl;
        }
        cout << "No duplicates found" << endl;
        return false;  // No duplicates found
    }
};