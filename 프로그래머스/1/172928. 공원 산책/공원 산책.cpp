#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(vector<string> park, vector<string> routes) {
    int H = park.size();
    int W = park[0].size();
    
    map<char, pair<int, int>> mp;
    mp['N'] = {-1, 0};
    mp['S'] = {1, 0};
    mp['W'] = {0, -1};
    mp['E'] = {0, 1};
    
    pair<int, int> loc;
    for (int i=0; i<H; i++) {
        for (int j=0; j<W; j++) {
            if (park[i][j] == 'S') loc = {i, j};
        }
    }
    
    for (const auto &route: routes) {
        char dir = route[0];
        int step = route[2] - '0';
        
        int ny = loc.first;
        int nx = loc.second;
        while(step--) {
            ny += mp[dir].first;
            nx += mp[dir].second;
            if (ny < 0 || nx < 0 || ny >= H || nx >= W) break;
            if (park[ny][nx] == 'X') break;
        }
        if (step < 0) loc = { ny, nx };
    }
    return { loc.first, loc.second };
    
}