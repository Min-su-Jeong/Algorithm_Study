#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>

using namespace std;

vector<int> solution(vector<string> keymap, vector<string> targets) {
    map<char, int> mp;
    vector<int> ret;

    for (int i = 0; i < keymap.size(); i++) {
        for (int j = 0; j < keymap[i].size(); j++) {
            char c = keymap[i][j];
            if (mp.count(c) == 0) mp[c] = j + 1;
            else mp[c] = min(mp[c], j + 1);
        }
    }

    for (string target: targets) {
        int sum = 0;

        for (char c: target) {
            if (mp.count(c) == 0) {
                sum = -1;
                break;
            }
            sum += mp[c];
        }
        ret.push_back(sum);
    }
    return ret;
}
