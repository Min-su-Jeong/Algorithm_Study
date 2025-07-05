#include <bits/stdc++.h>
using namespace std;

int T, K, a, b, ret;
string s[1004];

int findL(int pos) {
    for (int i=pos; i>=1; i--) {
        if (s[i][6] == s[i-1][2]) {
            return i;
        }
    }
    return 0;
}

int findR(int pos) {
    for (int i=pos; i<T-1; i++) {
        if (s[i][2] == s[i+1][6]) {
            return i;
        }
    }
    return T-1;
}

void rotateW(int pos, int dir) {
    if (dir) rotate(s[pos].begin(), s[pos].begin()+s[pos].size()-1, s[pos].end());
    else rotate(s[pos].begin(), s[pos].begin()+1, s[pos].end());
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> T; 
    for (int i=0; i<T; i++) cin >> s[i];

    cin >> K;
    for (int i=0; i<K; i++) {
        cin >> a >> b; a--;
        b = (b == -1 ? 0 : 1);
        int l = findL(a);
        int r = findR(a);
        int cnt = 0;
        for (int pos=a; pos>=l; pos--) {
            rotateW(pos, cnt % 2 == 0 ? b : !b);
            cnt++;
        }
        cnt = 1;
        for (int pos=a+1; pos<=r; pos++) {
            rotateW(pos, cnt % 2 == 0 ? b : !b);
            cnt++;
        }
    }
    for (int i=0; i<T; i++) {
        if (s[i][0] == '1') ret++;
    }
    cout << ret << '\n';

    return 0;
}