#include <bits/stdc++.h>
using namespace std;

int N, M, J, pos, ret;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M >> J;

    int l = 1, r = 1;
    for (int i=0; i<J; i++) {
        r = l + M - 1;

        cin >> pos;
        if (l <= pos && pos <= r) continue;
        else {
            if (pos < l) {
                ret += (l - pos);
                l = pos;
            } else {
                ret += (pos - r);
                l += pos - r;
            }
        }
    }
    cout << ret << '\n';
    return 0;
}