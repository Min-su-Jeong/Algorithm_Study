#include <bits/stdc++.h>
using namespace std;

const int INF = 987654321;
const int MAX = 54;
int N, M, a[MAX][MAX], ret = INF;
vector<pair<int, int>> home, chicken;
vector<vector<int>> selectedChicken;

void combi(int idx, vector<int> &v) {
    if (v.size() == M) {
        selectedChicken.push_back(v);
        return;
    }
    for (int i=idx+1; i<chicken.size(); i++) {
        v.push_back(i);
        combi(i, v);
        v.pop_back();
    }
}

int main() {
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> a[i][j];
            if (a[i][j] == 1) home.push_back({i, j});
            else if (a[i][j] == 2) chicken.push_back({i, j});
        }
    }

    vector<int> v;
    combi(-1, v);

    for (vector<int> ch: selectedChicken) {
        int sum = 0;
        for (auto h: home) {
            int mn = INF;
            for (int i: ch) {
                int dist = abs(h.first - chicken[i].first) + abs(h.second - chicken[i].second);
                mn = min(mn, dist);
            }
            sum += mn;
        }
        ret = min(ret, sum);
    }
    cout << ret << '\n';
    return 0;
}