#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MAX = 100000;
int N, K, visited[MAX+4];
ll cnt[MAX+4];

void bfs() {
    visited[N] = 1;
    cnt[N] = 1;
    queue<int> q;
    q.push(N);

    while(q.size()) {
        int x = q.front(); q.pop();
        for (int nx: {x-1, x+1, x*2}) {
            if (0 <= nx && nx <= MAX) {
                if (!visited[nx]) {
                    visited[nx] = visited[x] + 1;
                    cnt[nx] += cnt[x];
                    q.push(nx);
                } else if (visited[nx] == visited[x] + 1) {
                    cnt[nx] += cnt[x];
                }
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N >> K;
    if (N == K) {
        puts("0"); puts("1");
        return 0;
    }

    bfs();

    cout << visited[K] - 1 << '\n';
    cout << cnt[K] << '\n';
    return 0;
}