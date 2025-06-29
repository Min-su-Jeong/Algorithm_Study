#include <bits/stdc++.h>
using namespace std;

const int MAX = 51;
int N, K, words[MAX];
string s;

int count(int mask) {
    int cnt = 0;
    for (int word: words) {
        if (word && (word & mask) == word) cnt++;
    }
    return cnt;
}

int go(int idx, int K, int mask) {
    if (K < 0) return 0;
    if (idx == 26) return count(mask);
    int ret = go(idx+1, K-1, mask | (1 << idx));
    if (idx != 'a'-'a' && idx != 'n'-'a' && idx != 't'-'a' && idx != 'i'-'a' && idx != 'c'-'a') {
        ret = max(ret, go(idx+1, K, mask));
    }
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> K;
    for (int i=0; i<N; i++) {
        cin >> s;
        for (char c: s) words[i] |= (1 << (c - 'a'));
    }
    cout << go(0, K, 0) << '\n';

    return 0;
}