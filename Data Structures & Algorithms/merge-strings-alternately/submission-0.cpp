class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        //if (size(word1) || size(word2) ==0)return "";
        int length = max(size(word1), size(word2));
        string output = "";
        for(int i = 0; i < length; ++i){
            
            if (i < word1.size() ){output.push_back(word1[i]);}
            if (i < word2.size()){output.push_back(word2[i]);}
        }
        return output;
    }
};