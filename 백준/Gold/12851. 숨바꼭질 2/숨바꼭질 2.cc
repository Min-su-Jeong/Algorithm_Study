#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MAX = 100000;
int N, K, visited[MAX+4];
ll ret[MAX+4];

void bfs() {
    visited[N] = 1;
    ret[N] = 1;
    queue<int> q;
    q.push(N);
    
    while (q.size()) {
        int x = q.front();
        q.pop();
        for (int nx: {x-1, x+1, x << 1}) {
            if (nx < 0 || nx > MAX) continue;
            if (!visited[nx]) {
                visited[nx] = visited[x] + 1;
                ret[nx] += ret[x];
                q.push(nx);
            }
            else if (visited[nx] == visited[x] + 1) {
                ret[nx] += ret[x];
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> K;
    if (N == K) {
        puts("0"); puts("1");
        return 0;
    }

    bfs();

    cout << visited[K] - 1 << '\n';
    cout << ret[K] << '\n';
    return 0;
}