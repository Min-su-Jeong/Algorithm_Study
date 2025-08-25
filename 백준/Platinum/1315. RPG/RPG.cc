#include <bits/stdc++.h>
using namespace std;

struct Game {
    int x, y, c;
};

const int MAX = 1001;
int N, dp[MAX][MAX];
bool visited[MAX];
vector<Game> a;

int rpg(int STR, int INT) {
    int &ret = dp[STR][INT];
    if (ret != -1) return ret;

    ret = 0;
    int pnt = 0;
    vector<int> v;
    for (int i=0; i<N; i++) {
        if (a[i].x <= STR || a[i].y <= INT) {
            ret++;
            if (!visited[i]) {
                visited[i] = 1;
                pnt += a[i].c;
                v.push_back(i);
            }
        }
    }
    for (int p=0; p<=pnt; p++) {
        int nextSTR = min(1000, STR+p);
        int nextINT = min(1000, INT+pnt-p);
        ret = max(ret, rpg(nextSTR, nextINT));
    }
    for (int here: v) visited[here] = 0;

    return ret;
}

int main() {
    scanf("%d", &N);
    for (int i=0; i<N; i++) {
        int STR, INT, PNT;
        scanf("%d %d %d", &STR, &INT, &PNT);
        a.push_back({STR, INT, PNT});
    }
    memset(dp, -1, sizeof(dp));
    printf("%d\n", rpg(1, 1));

    return 0;
}