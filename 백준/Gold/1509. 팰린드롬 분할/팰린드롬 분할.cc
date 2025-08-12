#include <bits/stdc++.h>
using namespace std;

const int INF = 987654321;
const int MAX = 2504;
int dp[MAX][MAX], dp2[MAX];
string s;

int go(int here) {
    if (here == s.size()) return 0;
    if (dp2[here] != INF) return dp2[here];
    int &ret = dp2[here];
    for (int i=1; here+i<=s.size(); i++) {
        if (dp[here][i]) ret = min(ret, go(here + i) + 1);
    }
    return ret;
}

int main() {
    getline(cin, s);
    for (int i=0; i<s.size(); i++) dp[i][1] = 1;
    for (int i=0; i<s.size()-1; i++) {
        if (s[i] == s[i+1]) {
            dp[i][2] = 1;
        }
    }
    for (int _size=3; _size<=s.size(); _size++) {
        for (int i=0; i+_size <= s.size(); i++) {
            if (s[i] == s[i+_size-1] && dp[i+1][_size-2]) {
                dp[i][_size] = 1;
            }
        }
    }
    fill(dp2, dp2+MAX, INF);
    printf("%d", go(0));

    return 0;
}