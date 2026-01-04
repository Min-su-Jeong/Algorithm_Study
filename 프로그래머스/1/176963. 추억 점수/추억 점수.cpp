#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
    vector<int> ret;
    
    map<string, int> mp;
    for (int i=0; i<name.size(); i++) mp[name[i]] = yearning[i];
    
    for (vector<string> people: photo) {
        int sum = 0;
        for (string person: people) sum += mp[person];
        ret.push_back(sum);
    }
    return ret;
}