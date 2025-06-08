#include <bits/stdc++.h>
using namespace std;
#define prev pppp

const int MAX = 200004;
int N, K, ret, visited[MAX], prev[MAX];
vector<int> v;
queue<int> q;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N >> K;
    if (N == K) {
        cout << 0 << '\n' << N << '\n';
        return 0;
    }
    
    visited[N] = 1;
    q.push(N);
    
    while(q.size()) {
        int x = q.front(); q.pop();
        if (x == K) {
            ret = visited[K] - 1;
            break;
        }
        for (int nx: {x+1, x-1, x*2}) {
            if (nx >= MAX  || nx < 0 || visited[nx]) continue;
            visited[nx] = visited[x] + 1;
            prev[nx] = x;
            q.push(nx);
        }
    }
    
    for (int i=K; i != N; i=prev[i]) {
        v.push_back(i);
    }
    v.push_back(N);
    reverse(v.begin(), v.end());

    cout << ret << '\n';
    for (int i:v) cout << i << ' ';

    return 0;
}