#include <bits/stdc++.h>
using namespace std;

int N, K, tmp, psum[100001], ret = -10000004;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N >> K;
    for (int i=1; i<=N; i++) {
        cin >> tmp;
        psum[i] = psum[i-1] + tmp;
    }
    for (int i=K; i<=N; i++) {
        ret = max(ret, psum[i] - psum[i-K]);
    }

    cout << ret << "\n";
    return 0;
}