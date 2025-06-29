#include <bits/stdc++.h>
using namespace std;

const int MAX = 5;
int N, M, sum, ret, a[MAX][MAX];

int main() {
    scanf("%d %d", &N, &M);
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            scanf("%1d", &a[i][j]);
        }
    }

    for (int s=0; s < (1 << (N*M)); s++) {
        int sum = 0;

        // 가로
        for (int i=0; i<N; i++) {
            int cur = 0;
            for (int j=0; j<M; j++) {
                int k = i * M + j;
                if ((s & (1 << k)) == 0) {
                    cur = cur * 10 + a[i][j];
                } else {
                    sum += cur;
                    cur = 0;
                }
            }
            sum += cur;
        }

        // 세로
        for (int j=0; j<M; j++) {
            int cur = 0;
            for (int i=0; i<N; i++) {
                int k = i * M + j;
                if ((s & (1 << k)) != 0) {
                    cur = cur * 10 + a[i][j];
                } else {
                    sum += cur;
                    cur = 0;
                }
            }
            sum += cur;
        }
        ret = max(ret, sum);
    }
    printf("%d", ret);

    return 0;
}