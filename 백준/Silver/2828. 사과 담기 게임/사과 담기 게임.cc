#include <bits/stdc++.h>
using namespace std;

int M, N, J, l, r, pos, ret;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    cin >> N >> M >> J;
    l = 1;
    for (int i=0; i<J; i++) {
        r = l + M - 1;
        
        cin >> pos;
        if (l <= pos && pos <= r) continue;
        else {
            if (pos < l) {
                ret += (l - pos);
                l = pos;
            } else {
                l += (pos - r);
                ret += (pos - r);
            }
        }
    }
    cout << ret << '\n';

    return 0;
}