#include <bits/stdc++.h>
using namespace std;

const int MAX = 21;
const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {-1, 0, 1, 0};
int R, C, ret;
char a[MAX][MAX];

void go(int y, int x, int num, int cnt) {
    ret = max(ret, cnt);
    for (int i=0; i<4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (ny < 0 || nx < 0 || ny >= R || nx >= C) continue;
        int _next = 1 << (int)(a[ny][nx] - 'A');
        if ((num & _next) == 0) go(ny, nx, num | _next, cnt+1);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> R >> C;
    for(int i=0; i<R; i++) {
        for (int j=0; j<C; j++) {
            cin >> a[i][j];
        }
    }
    go(0, 0, 1 << (int)(a[0][0] - 'A'), 1);
    cout << ret << '\n';
    return 0;
}