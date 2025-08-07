#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int N, K, num, ret=-INT_MAX;
    cin >> N >> K;

    int psum[N];
    memset(psum, 0, sizeof(psum));
    for (int i=1; i<=N; i++) {
        cin >> num;
        psum[i] = psum[i-1] + num;
    }

    for (int i=K; i<=N; i++) {
        ret = max(ret, psum[i] - psum[i-K]);
    }
    cout << ret << '\n';
    
    return 0;
}