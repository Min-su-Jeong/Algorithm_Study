#include <bits/stdc++.h>
using namespace std;

const int MAX = 104;
int N, L, ret, a[MAX][MAX], b[MAX][MAX];

void solve(int a[MAX][MAX]) {
    for (int i=0; i<N; i++) {
        int cnt = 1;
        int j;
        for (j=0; j<N-1; j++) {
            if (a[i][j] == a[i][j+1]) cnt++;
            else if (a[i][j]+1 == a[i][j+1] && cnt >= L) cnt = 1;
            else if (a[i][j]-1 == a[i][j+1] && cnt >= 0) cnt = -L+1;
            else break;
        }
        if (j == N-1 && cnt >= 0) ret++;
    }
    return;
}

int main() {
    scanf("%d %d", &N, &L);
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            scanf("%d", &a[i][j]);
            b[j][i] = a[i][j];
        }
    }
    solve(a); solve(b);
    cout << ret<< '\n';

    return 0;
}