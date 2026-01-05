#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> wallpaper) {
    int H = wallpaper.size();
    int W = wallpaper[0].size();
    
    vector<int> ret = { 51, 51, 0, 0 };
    
    for (int i=0; i<H; i++) {
        for (int j=0; j<W; j++) {
            if (wallpaper[i][j] == '#') {
                ret[0] = min(ret[0], i); // lux
                ret[1] = min(ret[1], j); // luy
                ret[2] = max(ret[2], i+1); // rux
                ret[3] = max(ret[3], j+1); // ruy
            }
        }
    }
    return ret;
}