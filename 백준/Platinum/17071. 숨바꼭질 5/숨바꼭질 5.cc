#include <bits/stdc++.h>
using namespace std;

const int MAX = 500000;
int N, K, visited[2][MAX+4], ret = 1;
bool flag;

void bfs() {
    visited[0][N] = 1;
    queue<int> q;
    q.push(N);

    while (q.size()) {
        K += ret;
        if (K > MAX) break;
        if (visited[ret%2][K]) {
            flag = true;
            break;
        }
        int qSize = q.size();
        for (int i=0; i<qSize; i++) {
            int x = q.front(); q.pop();
            for (int nx: {x+1, x-1, x*2}) {
                if (nx < 0 || nx > MAX || visited[ret%2][nx]) continue;
                visited[ret%2][nx] = visited[(ret+1)%2][x] + 1;
                if (nx == K) {
                    flag = 1;
                    break;
                }
                q.push(nx);
            }
            if (flag) break;
        }
        if (flag) break;
        ret++;
    }
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N >> K;
    if (N == K) {
        cout << 0 << '\n';
        return 0;
    }

    bfs();

    if (flag) cout << ret << '\n';
    else cout << -1 << '\n';
    return 0;
}