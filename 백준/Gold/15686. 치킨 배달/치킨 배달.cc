#include <bits/stdc++.h>
using namespace std;

const int MAX = 51;
int N, M, a[MAX][MAX], ret=987654321;
vector<vector<int>> selectedChicken;
vector<pair<int, int>> chicken, home;

void comb(int start, vector<int> v) {
    if (v.size() == M) {
        selectedChicken.push_back(v);
        return;
    }
    for (int i=start+1; i<chicken.size(); i++) {
        v.push_back(i);
        comb(i, v);
        v.pop_back();
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> a[i][j];
            if (a[i][j] == 1) home.push_back({i, j});
            if (a[i][j] == 2) chicken.push_back({i, j});
        }
    }

    vector<int> v;
    comb(-1, v);
    for (vector<int> selected: selectedChicken) {
        int sum = 0;
        for (auto h: home) {
            int mn = 987654321;
            for (int i: selected) {
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