#include <bits/stdc++.h>
using namespace std;

const int MAX = 51;
int N, M, graph[MAX][MAX], result = INT_MAX;
vector<vector<int>> chickenList;
vector<pair<int, int>> home, chicken;

void combi(int start, vector<int> v) {
    if (v.size() == M) {
        chickenList.push_back(v);
        return;
    }

    for (int i=start+1; i<chicken.size(); i++) {
        v.push_back(i);
        combi(i, v);
        v.pop_back();
    }
    return;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> graph[i][j];
            if (graph[i][j] == 1) home.push_back({i, j});
            if (graph[i][j] == 2) chicken.push_back({i, j});
        }
    }

    vector<int> v;
    combi(-1, v);
    for (vector<int> cList: chickenList) {
        int ret = 0;
        for (pair<int, int> h: home) {
            int _min = INT_MAX;
            for (int ch: cList) {
                int _dist = abs(h.first - chicken[ch].first) + abs(h.second - chicken[ch].second);
                _min = min(_min, _dist);
            }
            ret += _min;
        }
        result = min(result, ret);
    }
    cout << result << '\n';

    return 0;
}