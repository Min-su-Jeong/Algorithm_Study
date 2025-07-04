#include <bits/stdc++.h>
using namespace std;

const int MAX = 104;
const int dx[4] = {0, 1, 0, -1};
const int dy[4] = {-1, 0, 1, 0};
int N, K, L, y, x, t, idx, ret, dir = 1;
int a[MAX][MAX], visited[MAX][MAX];
char c;
deque<pair<int, int>> dq;
vector<pair<int, int>> _time;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL); 

    cin >> N >> K;
    for (int i=0; i<K; i++) {
        cin >> y >> x;
        a[--y][--x] = 1;
    }
    cin >> L;
    for (int i=0; i<L; i++) {
        cin >> t >> c;
        if (c == 'D') _time.push_back({t, 1});
        else _time.push_back({t, 3});
    }

    dq.push_back({0, 0});
    while (dq.size()) {
        ret++;
        tie(y, x) = dq.front();
        int ny = y + dy[dir];
        int nx = x + dx[dir];
        if (ny < 0 || ny >= N || nx < 0 || nx >= N || visited[ny][nx]) break;
        if (!a[ny][nx]) {
            visited[dq.back().first][dq.back().second] = 0;
            dq.pop_back();
        } else a[ny][nx] = 0;

        visited[ny][nx] = 1;
        dq.push_front({ny, nx});
        if (ret == _time[idx].first) {
            dir = (dir + _time[idx].second) % 4;
            idx++;
        }
    }
    cout << ret << '\n';

    return 0;
}