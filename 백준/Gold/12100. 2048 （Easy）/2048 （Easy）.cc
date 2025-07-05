#include <bits/stdc++.h>
using namespace std;

const int MAX = 21;
int N, ret;

struct Board {
    int a[MAX][MAX];

    void _rotate90() {
        int tmp[MAX][MAX];
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                tmp[i][j] = a[N-j-1][i];
            }
        }
        memcpy(a, tmp, sizeof(a));
    }

    void _move() {
        int tmp[MAX][MAX];
        for (int i=0; i<N; i++) {
            int c = -1, d = 0;
            for (int j=0; j<N; j++) {
                if (a[i][j] == 0) continue;
                if (d && a[i][j] == tmp[i][c]) tmp[i][c] *= 2, d = 0;
                else tmp[i][++c] = a[i][j], d = 1;
            }
            for (c++; c<N; c++) tmp[i][c] = 0;
        }
        memcpy(a, tmp, sizeof(a));
    }

    void getMAX() {
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                ret = max(ret, a[i][j]);
            }
        }
    }
};

void go(Board b, int here) {
    if (here == 5) {
        b.getMAX();
        return;
    }
    for (int i=0; i<4; i++) {
        Board c = b;
        c._move();
        go(c, here+1);
        b._rotate90();
    }
    return;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    Board b;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> b.a[i][j];
        }
    }
    go(b, 0);
    cout << ret << '\n';

    return 0;
}