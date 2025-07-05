#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second

const int MAX = 104;
const int INF = 1e9;
const int dx[4] = {1, 0, -1, 0};
const int dy[4] = {0, 1, 0, -1};
int N, M, K, r, c, s, ret = INF;
int a[MAX][MAX], b[MAX][MAX], visited[MAX][MAX];

struct A {
    int y, x, cnt;
};
vector<A> v;
vector<int> v_idx;
vector<pair<int, int>> vv;

int sy, sx, ey, ex, dir;

void go(int y, int x, int first) {
    if (!first && y == sy && x == sx) return;

    int ny = y + dy[dir];
    int nx = x + dx[dir];
    if (ny < sy || ny > ey || nx < sx || nx > ex) {
        dir = (dir + 1) % 4;
        ny = y + dy[dir];
        nx = x + dx[dir];
    }

    vv.push_back({ny, nx});
    go(ny, nx, 0);
}

void rotateOne(int y, int x, int cnt) {
    for (int i = 1; i <= cnt; i++) {
        sy = y - i;
        sx = x - i;
        ey = y + i;
        ex = x + i;
        vv.clear();
        dir = 0;
        vv.push_back({sy, sx});
        go(sy, sx, 1);

        vector<int> tmp;
        for (auto [y, x] : vv) tmp.push_back(b[y][x]);
        rotate(tmp.rbegin(), tmp.rbegin() + 1, tmp.rend());

        for (int i = 0; i < vv.size(); i++) {
            b[vv[i].f][vv[i].s] = tmp[i];
        }
    }
}

int solve() {
    for (int i : v_idx) {
        rotateOne(v[i].y, v[i].x, v[i].cnt);
    }
    int mn = INF;
    for (int i = 0; i < N; i++) {
        int sum = 0;
        for (int j = 0; j < M; j++) {
            sum += b[i][j];
        }
        mn = min(mn, sum);
    }
    return mn;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M >> K;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            cin >> a[i][j];

    for (int i = 0; i < K; i++) {
        cin >> r >> c >> s;
        r--; c--;
        v.push_back({r, c, s});
        v_idx.push_back(i);
    }

    do {
        memcpy(b, a, sizeof(a));
        ret = min(ret, solve());
    } while (next_permutation(v_idx.begin(), v_idx.end()));

    cout << ret << '\n';
    return 0;
}