#include <bits/stdc++.h>
using namespace std;

const int INF = 987654321;
const int MAX = 104;
int a[MAX][MAX], ret=INF, n=10;
map<int, int> mp;

bool check(int y, int x, int cnt) {
    if (y + cnt > n || x + cnt > n) return false;
    for (int i=y; i<y+cnt; i++) {
        for (int j=x; j<x+cnt; j++) {
            if (a[i][j] == 0) return false;
        }
    }
    return true;
}

void draw(int y, int x, int cnt, int val) {
    for (int i=y; i<y+cnt; i++) {
        for (int j=x; j<x+cnt; j++) {
            a[i][j] = val; 
        }
    }
}

void dfs(int y, int x, int cnt) {
    // 가지치기
    if (cnt >= ret) return;
    if (x == n) {
        dfs(y+1, 0, cnt);
        return;
    }
    if (y == n) {
        ret = min(ret, cnt);
        return;
    }
    if (a[y][x] == 0) {
        dfs(y, x+1, cnt);
        return;
    }
    for (int s=5; s>=1; s--) {
        if(mp[s] == 5) continue;
        if (check(y, x, s)) {
            mp[s]++;
            draw(y, x, s, 0);
            dfs(y, x + s, cnt+1);
            draw(y, x, s, 1);
            mp[s]--;
        }
    }
    return;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> a[i][j];
        }
    }
    dfs(0, 0, 0);
    
    cout << (ret == INF ? -1 : ret) << '\n';
    return 0; 
}