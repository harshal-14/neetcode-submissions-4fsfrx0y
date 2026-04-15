/*
Approach: iterate thru strs, use a delimiter to keep them together
*/

class Solution {
public:

    string encode(vector<string>& strs) {
        char delimiter = '/';
        std::string encoded;
        for(auto &str:strs){
            // encoded.push_back(str);
            // for(auto &enc:encoded){cout<<encoded[enc]<<"\n";}
            encoded+=str+delimiter;
        }
        return encoded;
    }

    vector<string> decode(string s) {
        std::vector<string> decoded;
        std::string tempstr;
        char delimiter = '/';
        for(auto &c:s){
            // tempstr.insert(c);
            if(c!=delimiter){
                // decoded.push_back(tempstr);
                tempstr.push_back(c);
                // tempstr.clear();
            }
            else{
                decoded.push_back(tempstr);
                tempstr.clear();
            }
        }
        return decoded; 
    }
};
