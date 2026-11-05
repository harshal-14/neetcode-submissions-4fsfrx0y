class MyHashSet {                 // define a new type called MyHashSet
private:                          // what follows is hidden from outside code
    vector<int> data;             // a growable list of ints; this holds the set's keys
public:                           // what follows can be called by LeetCode
    MyHashSet() {}                // constructor: runs when the object is created; does nothing (list starts empty)

    void add(int key) {                                      // add a key; returns nothing
        if (find(data.begin(), data.end(), key) == data.end()) {   // search the list for key; "== end()" means NOT found
            data.push_back(key);                             // so append key to the back of the list
        }
    }

    void remove(int key) {                                   // remove a key; returns nothing
        auto it = find(data.begin(), data.end(), key);       // search for key; "it" = the position where it was found
        if (it != data.end()) {                              // "!= end()" means it WAS found
            data.erase(it);                                  // delete the item at that position
        }
    }

    bool contains(int key) {                                 // returns true or false
        return find(data.begin(), data.end(), key) != data.end();  // true if found, false if not
    }
};                                // a class must end with a semicolon